import logging
import json
from account.controller import constants
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from account.implementation import accountlogic
from account.authentication import isAunthenticated


class Register(GenericAPIView):

    def post(self, request):

        response = {'payload': {}, "status": 200, "error": [], "message": ""}

        try:
            response = accountlogic.register(request, response)

        except Exception as e:
            logging.exception(str(e))
            response["status"] = constants.FAILURE_STATUS
            response['message'] = constants.REGISTER_FAILURE_MESSAGE

        return Response(response)


class Login(GenericAPIView):

    def post(self, request):

        request = json.load(request)
        response = {'payload': {}, "status": 200, "error": [], "message": ""}

        try:
            response = accountlogic.login(request, response)

        except Exception as e:
            logging.exception(str(e))
            response['message'] = constants.LOGIN_FAILURE_MESSAGE
            response['status'] = constants.AUTH_FAILURE_STATUS

        return Response(response)


class AddPatient(GenericAPIView):

    def post(self, request):

        try:

            permission = isAunthenticated(token=request.META[constants.HTTP_AUTHORIZATION])
            request = json.load(request)
            response = {'payload': {}, "status": 200, "error": [], "message": ""}

            if permission:

                response = accountlogic.addpatient(request, response)

            else:
                response["status"] = constants.AUTH_FAILURE_STATUS
                response['message'] = constants.AUTHENTICATION_FAILED

        except Exception as e:

            logging.exception(str(e))
            response["status"] = constants.FAILURE_STATUS
            response['message'] = constants.PATIENT_FAILURE_MESSAGE

        return JsonResponse(response)


class ListPatient(GenericAPIView):

    def post(self, request):

        try:

            permission = isAunthenticated(token=request.META[constants.HTTP_AUTHORIZATION])

            request = json.load(request)
            response = {'payload': {}, "status": 200, "error": [], "message": ""}

            if permission:

                response = accountlogic.listpatient(request, response)

            else:
                response["status"] = constants.AUTH_FAILURE_STATUS
                response['message'] = constants.AUTHENTICATION_FAILED

        except Exception as e:

            logging.exception(str(e))
            response["status"] = constants.FAILURE_STATUS
            response['message'] = constants.PATIENT_LIST_FAILURE_MESSAGE

        return JsonResponse(response)


class UpdateProfile(GenericAPIView):

    def post(self, request):

        try:

            permission = isAunthenticated(token=request.META[constants.HTTP_AUTHORIZATION])

            request = json.load(request)
            response = {'payload': {}, "status": 200, "error": [], "message": ""}

            if permission:

                response = accountlogic.updateprofile(request, response)

            else:
                response["status"] = constants.AUTH_FAILURE_STATUS
                response['message'] = constants.AUTHENTICATION_FAILED

        except Exception as e:

            logging.exception(str(e))
            response["status"] = constants.FAILURE_STATUS
            response['message'] = constants.UPDATE_FAILURE_MESSAGE

        return JsonResponse(response)


class SelectLanguages(GenericAPIView):

    def post(self, request):

        try:

            permission = isAunthenticated(token=request.META[constants.HTTP_AUTHORIZATION])

            request = json.load(request)
            response = {'payload': {}, "status": 200, "error": [], "message": ""}

            if permission:

                response = accountlogic.selectlanguages(request, response)

            else:
                response["status"] = constants.AUTH_FAILURE_STATUS
                response['message'] = constants.AUTHENTICATION_FAILED

        except Exception as e:

            logging.exception(str(e))
            response["status"] = constants.FAILURE_STATUS
            response['message'] = constants.LANGUAGE_FAILURE_MESSAGE

        return JsonResponse(response)

