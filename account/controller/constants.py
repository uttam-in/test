SUCCESS_STATUS = 200
FAILURE_STATUS = 400
AUTH_FAILURE_STATUS = 401
HTTP_AUTHORIZATION = 'HTTP_AUTHORIZATION'
AUTHENTICATION_FAILED = 'Invalid token'
DoctorList = ['email', 'password', 'phone']
ProfileList = ['spoken_languages', 'diplomas']

# Register API

REGISTER_SUCCESS_MESSAGE = "Registered Successfully"
REGISTER_FAILURE_MESSAGE = "Registration Failed - Please fill all the required details with proper format"

# Login API

LOGIN_SUCCESS_MESSAGE = "Log-in Success"
LOGIN_FAILURE_MESSAGE = "Unable to login with the given credentials - Unauthorized"

# addpatient

PATIENT_SUCCESS_MESSAGE = "Patient added successfully"
PATIENT_FAILURE_MESSAGE = "Failed to add patient - give proper details"

# listpatient

PATIENT_LIST_SUCCESS_MESSAGE = "Patient fetched successfully"
PATIENT_LIST_FAILURE_MESSAGE = "Failed to fetch patient details"

# updateprofile

UPDATE_SUCCESS_MESSAGE = "Updated successfully"
UPDATE_FAILURE_MESSAGE = "Failed to update the profile - update values should be in proper format"

# selectlanguages

LANGUAGE_SUCCESS_MESSAGE = "Spoken language details"
LANGUAGE_FAILURE_MESSAGE = "Failed to fetch spoken language details for a given doctor"
