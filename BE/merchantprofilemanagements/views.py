from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, parser_classes
from rest_framework.renderers import JSONRenderer
from . import models, contants, validates


# author: nmcuong
# output: object
# function: get_table_merchant_profile.
# description: load data in table merchant profile.
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def get_table_merchant_profile(request, format=None):
    response = contants.get_response_get_table_merchant_profile(None)
    try:
        data_output = models.get_table_merchant_profile()

        code_output = data_output['code']
        table_data = data_output['table_data']

        response = contants.get_response_get_table_merchant_profile(code_output)
        response['table_data'] = table_data

    except Exception as e:
        print('merchantprofilemanagements.views -> get_table_merchant_profile -> ex: ', e)

    return Response(response)


# author: nmcuong
# function: search_table_merchant_profile.
# description: search data in table merchant profile.
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def search_table_merchant_profile(request, format=None):
    response = contants.get_response_search_table_merchant_profile(None)
    try:
        data_input = request.data
        merchant_name = data_input['merchant_name']
        abbreviation = data_input['abbreviation']
        language = data_input['language']
        status = data_input['status']

        merchant_name.strip()
        abbreviation.strip()

        data_output = models.search_table_merchant_profile(merchant_name, abbreviation, language, status)

        code_output = data_output['code']
        table_data = data_output['table_data']

        response = contants.get_response_get_table_merchant_profile(code_output)
        response['table_data'] = table_data

    except Exception as e:
        print('merchantprofilemanagements.views -> search_table_merchant_profile -> ex: ', e)

    return Response(response)


# author: nmcuong
# function: get_combobox_language.
# description: load data in combo box language merchant profile.
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def get_combobox_language(request, format=None):
    response = contants.get_response_get_combobox_language(None)
    try:
        data_output = models.get_combobox_language()

        code_output = data_output['code']
        table_data = data_output['table_data']

        response = contants.get_response_get_combobox_language(code_output)
        response['code'] = code_output
        response['table_data'] = table_data

    except Exception as e:
        print('merchantprofilemanagements.views -> get_combobox_language -> ex: ', e)

    return Response(response)


# author: nmcuong
# function: delete_merchant_profile.
# description: delete data in table merchant profile.
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def delete_merchant_profile(request):
    response = contants.get_response_delete_merchant_profile(None)
    try:
        data_input = request.data
        profile_info_id = data_input['rowID']

        data_output = models.delete_merchant_profile(profile_info_id)

        code_output = data_output['code']

        response = contants.get_response_delete_merchant_profile(code_output)

    except Exception as e:
        print('merchantprofilemanagements.views -> search_table_merchant_profile -> ex: ', e)

    return Response(response)


# author: nmcuong
# function: init_create_profile_information.
# description: init screen create merchant profile.
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def init_create_profile_information(request, format=None):
    response = contants.get_response_init_create_profile_information(None)
    try:
        data_output = models.init_create_profile_information()
        code_output = data_output['code']
        currency_data = data_output['currency_data']
        country_data = data_output['country_data']
        language_data = data_output['language_data']
        response = contants.get_response_init_create_profile_information(code_output)
        response['currency_data'] = currency_data
        response['country_data'] = country_data
        response['language_data'] = language_data
    except Exception as e:
        print('merchantprofilemanagements.views -> init_create_profile_information -> ex: ', e)

    return Response(response)


# author: nmcuong
# function: create_profile_information.
# description: create profile information in module create merchant profile.
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def create_profile_information(request, format=None):
    response = contants.get_response_create_profile_information(None)
    try:
        data_input = request.data
        validate_profile_out_code = validates.validation_create_profile(data_input)
        if validate_profile_out_code == 0:
            data_output = models.create_profile_information(request, data_input)
            code_output = data_output['code']
            response = contants.get_response_create_profile_information(code_output)

    except Exception as e:
        print('merchantprofilemanagements.views -> create_profile_information -> ex: ', e)

    return Response(response)


# author: nmcuong
# function: search_table_merchant_profile.
# description: search data in table merchant profile.
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def init_profile_information_detail(request, format=None):
    response = contants.get_response_init_profile_information_detail(None)
    try:
        data_input = request.data
        profile_info_id = data_input['rowID']
        print("row ID: ", profile_info_id)

        data_output = models.init_profile_information_detail(profile_info_id)

        code_output = data_output['code']
        profile_info_data = data_output['profile_info_data']
        contact_data = data_output['contact_data']
        features_data = data_output['features_data']
        fee_data = data_output['fee_data']

        response = contants.get_response_get_table_merchant_profile(code_output)
        response['profile_info_data'] = profile_info_data
        response['contact_data'] = contact_data
        response['features_data'] = features_data
        response['fee_data'] = fee_data

    except Exception as e:
        print('merchantprofilemanagements.views -> init_profile_information_detail -> ex: ', e)

    return Response(response)