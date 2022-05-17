import json
import logging
import jwt, datetime
from account.controller import constants
from account.models import Profile, Patient, Doctor
from account.serializers import PatientSerializer, ProfileSerializer


def register(request, response):

    try:
        if request:

            email = request.data['email']
            phone = request.data['phone']
            password = request.data['password']
            birthdate = request.data['birthdate']
            gender = request.data['gender']
            location = request.data['location']
            spoken_languages = json.loads(request.data['spoken_languages'])
            diplomas = json.loads(request.data['diplomas'])
            picture = request.data['picture']

            obj_doct = Doctor(email=email, phone=phone, password=password)
            obj_doct.save()

            obj_prof = Profile(birthdate=birthdate, gender=gender, location=location,
                               spoken_languages=spoken_languages, diplomas=diplomas, picture=picture,
                               doctor=obj_doct)
            obj_prof.save()

            response["status"] = constants.SUCCESS_STATUS
            response['message'] = constants.REGISTER_SUCCESS_MESSAGE

    except Exception as e:
        logging.exception(str(e))
        response["status"] = constants.FAILURE_STATUS
        response['message'] = constants.REGISTER_FAILURE_MESSAGE

    return response


def login(request, response):

    try:
        if request:

            email = request.get("email", "")
            password = request.get("password", "")

            user = Doctor.objects.filter(email=email, password=password).first()

            if user:
                payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                    'iat': datetime.datetime.utcnow()
                }

                token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
                response['token'] = token
                response['message'] = constants.LOGIN_SUCCESS_MESSAGE
                response['status'] = constants.SUCCESS_STATUS

            else:
                response['message'] = constants.LOGIN_FAILURE_MESSAGE
                response['status'] = constants.AUTH_FAILURE_STATUS

    except Exception as e:

        logging.exception(str(e))
        response['message'] = constants.LOGIN_FAILURE_MESSAGE
        response['status'] = constants.AUTH_FAILURE_STATUS

    return response


def addpatient(request, response):

    try:
        if request:

            first_name = request.get("first_name", "")
            last_name = request.get("last_name", "")
            birthdate = request.get("birthdate", "")
            email = request.get("email", "")
            doctor = request.get("doctor", "")

            obj_doc = Doctor.objects.get(pk=doctor)

            if obj_doc:
                obj = Patient(first_name=first_name, last_name=last_name, birthdate=birthdate,
                              email=email, doctor=obj_doc)
                obj.save()

                response["status"] = constants.SUCCESS_STATUS
                response['message'] = constants.PATIENT_SUCCESS_MESSAGE

    except Exception as e:
        logging.exception(str(e))
        response["status"] = constants.FAILURE_STATUS
        response['message'] = constants.PATIENT_FAILURE_MESSAGE

    return response


def listpatient(request, response):

    try:
        if request:

            doctor = request.get("doctor", "")
            obj_doc = Doctor.objects.get(pk=doctor)

            if obj_doc:

                payload_data = Patient.objects.filter(doctor=obj_doc).all()
                serializer = PatientSerializer(payload_data, many=True)

                response["payload"] = serializer.data
                response["status"] = constants.SUCCESS_STATUS
                response['message'] = constants.PATIENT_LIST_SUCCESS_MESSAGE

    except Exception as e:
        logging.exception(str(e))
        response["status"] = constants.FAILURE_STATUS
        response['message'] = constants.PATIENT_LIST_FAILURE_MESSAGE

    return response


def updateprofile(request, response):

    try:
        if request:

            doctor = request.get("doctor", "")

            doct_dict = {}
            profile_dict = {}
            for field, value in request.items():
                if field in constants.DoctorList:
                    doct_dict[field] = value
                elif field in constants.ProfileList:
                    profile_dict[field] = json.loads(value)
                else:
                    profile_dict[field] = value

            doct_dict['id'] = doctor

            Doctor.objects.filter(pk=doctor).update(**doct_dict)

            obj_doc = Doctor.objects.get(pk=doctor)

            if obj_doc:

                Profile.objects.filter(doctor=obj_doc).update(**profile_dict)

            response["status"] = constants.SUCCESS_STATUS
            response['message'] = constants.UPDATE_SUCCESS_MESSAGE

    except Exception as e:
        logging.exception(str(e))
        response["status"] = constants.FAILURE_STATUS
        response['message'] = constants.UPDATE_FAILURE_MESSAGE

    return response


def selectlanguages(request, response):

    try:
        if request:

            doctor = request.get("doctor", "")
            obj_doc = Doctor.objects.get(pk=doctor)

            if obj_doc:

                payload_data = Profile.objects.filter(doctor=obj_doc).all()
                serializer = ProfileSerializer(payload_data, many=True)

                response["payload"] = serializer.data
                response["status"] = constants.SUCCESS_STATUS
                response['message'] = constants.LANGUAGE_SUCCESS_MESSAGE

    except Exception as e:
        logging.exception(str(e))
        response["status"] = constants.FAILURE_STATUS
        response['message'] = constants.LANGUAGE_FAILURE_MESSAGE

    return response
