from rest_framework import status


def get_response_get_table_merchant_profile(code):
    response = {
        'code': 999,
        'message': 'An error has occurred. Please contact the administrator.',
        'status_code': status.HTTP_200_OK
    }

    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Get data table in successfully'

    return response


def get_response_search_table_merchant_profile(code):
    response = {
        'code': 999,
        'message': 'An error has occurred. Please contact the administrator.',
        'status_code': status.HTTP_200_OK
    }

    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Search data table successfully'

    return response


def get_response_get_combobox_language(code):
    response = {
        'code': 999,
        'message': 'An error has occurred. Please contact the administrator.',
        'status_code': status.HTTP_200_OK
    }

    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'get data combo box language successfully'

    return response


def get_response_delete_merchant_profile(code):
    response = {
        'code': 999,
        'message': 'An error has occurred. Please contact the administrator.',
        'status_code': status.HTTP_200_OK
    }

    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'delete data merchant profile successfully.'

    return response


def get_response_create_profile_information(code):
    response = {
        'code': 999,
        'message': 'An error has occurred. Please contact the administrator.',
        'status_code': status.HTTP_200_OK
    }

    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Create merchant profile successfully.'
        elif code == 'SUC_AR11_01':
            response['message'] = 'Create merchant profile successfully.'
        elif code == 'ERR_AR11_02':
            response['message'] = 'Please input Merchant ID value.'
        elif code == 'ERR_AR11_03':
            response['message'] = 'Please input MCC value.'
        elif code == 'ERR_AR11_04':
            response['message'] = 'Please input Based Currency value.'
        elif code == 'ERR_AR11_05':
            response['message'] = 'Please input Base Country value.'
        elif code == 'ERR_AR11_06':
            response['message'] = 'Please input Merchant Name value.'
        elif code == 'ERR_AR11_07':
            response['message'] = 'Please input Default language value.'
        elif code == 'ERR_AR11_08':
            response['message'] = 'Please input Abbreviation value.'
        elif code == 'ERR_AR11_09':
            response['message'] = 'Please input Tax ID value.'
        elif code == 'ERR_AR11_10':
            response['message'] = 'Please input Profile Status value.'
        elif code == 'ERR_AR11_11':
            response['message'] = 'Please input TID value.'
        elif code == 'ERR_AR11_12':
            response['message'] = 'Please input Website URL value.'
        elif code == 'ERR_AR11_13':
            response['message'] = 'Please input DBA Name value.'
        elif code == 'ERR_AR11_14':
            response['message'] = 'Please input Street Name value.'
        elif code == 'ERR_AR11_15':
            response['message'] = 'Please input State value.'
        elif code == 'ERR_AR11_16':
            response['message'] = 'Please input City value.'
        elif code == 'ERR_AR11_17':
            response['message'] = 'Please input Phone Number value.'
        elif code == 'ERR_AR11_18':
            response['message'] = 'Please input Setup Charge value.'
        elif code == 'ERR_AR11_19':
            response['message'] = 'Please input Annual Charge value.'
        elif code == 'ERR_AR11_20':
            response['message'] = 'Please input Per Transaction Fee (Fix) value.'
        elif code == 'ERR_AR11_21':
            response['message'] = 'Please input Per Successful Rate value.'
        elif code == 'ERR_AR11_22':
            response['message'] = 'Please input Per Transaction Rate (%) Refund value.'
        elif code == 'ERR_AR11_23':
            response['message'] = 'Please input Comments value.'

    return response


def get_response_init_create_profile_information(code):
    response = {
        'code': 999,
        'message': 'An error has occurred. Please contact the administrator.',
        'status_code': status.HTTP_200_OK
    }

    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'init create profile information successfully'

    return response


def get_response_init_profile_information_detail(code):
    response = {
        'code': 999,
        'message': 'An error has occurred. Please contact the administrator.',
        'status_code': status.HTTP_200_OK
    }

    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'init profile information detail successfully'

    return response
