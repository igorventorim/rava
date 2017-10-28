import requests
from authentication import Authentication
from strings import Strings
import json


# THIS CLASS CONFIGURE FEATURES AT MESSENGER PROFILE
class MessengerProfile():

    def __init__(self):
        self.__urlProfile = "https://graph.facebook.com/v2.6/me/messenger_profile"
        self.__headers = {"Content-Type": "application/json"}
        self.__params = {"access_token": Authentication.PAGE_ACCESS_TOKEN}



    # ------ GET STARTED BUTTON ------
    # https://developers.facebook.com/docs/messenger-platform/messenger-profile/get-started-button

    def createStartedButton(self):
        data = json.dumps({"get_started":{ "payload":Strings.GET_STARTED} })
        result = json.loads(requests.post(self.__urlProfile,params=self.__params,headers=self.__headers,data=data).text)
        return result["result"] == "success"

    def checkStartedButton(self):
        params = {"access_token": Authentication.PAGE_ACCESS_TOKEN,"fields":"get_started"}
        result = json.loads(requests.get(self.__urlProfile,params=params).text)
        return result

    def deleteStartedButton(self):
        data = json.dumps({"fields":["get_started"]})
        result = json.loads(requests.delete(self.__urlProfile,headers=self.__headers,params=self.__params,data=data).text)
        return result["result"] == "success"


    # ------ GREETING TEXT ------
    # https://developers.facebook.com/docs/messenger-platform/messenger-profile/greeting-text
    def createGreeting(self):
        data = { "greeting":[ { "locale":"default", "text":Strings.GREETING} ] }
        result = json.loads(requests.post(self.__urlProfile,params=self.__params,headers=self.__headers,data=data).text)
        print(result)
        return result["result"] == "success"

    def readGreeting(self):
        params = {"access_token": Authentication.PAGE_ACCESS_TOKEN, "fields": "greeting"}
        result = json.loads(requests.get(self.__urlProfile, params=params).text)
        return result

    def deleteGreeting(self):
        data = json.dumps({"fields": ["greeting"]})
        result = json.loads(requests.delete(self.__urlProfile, headers=self.__headers, params=self.__params, data=data).text)
        return result["result"] == "success"



    # ------ MENU PERSISTENTE ------
    # https://developers.facebook.com/docs/messenger-platform/messenger-profile/persistent-menu

    def createMenu(self):
        data = json.dumps({
                          # TODO: Definir Estrutura do menu
                          # "persistent_menu":[
                          #   {
                          #     "locale":"default",
                          #     "composer_input_disabled":False,
                          #     "call_to_actions":[
                          #       {
                          #         "title":"My Account",
                          #         "type":"nested",
                          #         "call_to_actions":[
                          #           {
                          #             "title":"Pay Bill",
                          #             "type":"postback",
                          #             "payload":"PAYBILL_PAYLOAD"
                          #           },
                          #           {
                          #             "title":"History",
                          #             "type":"postback",
                          #             "payload":"HISTORY_PAYLOAD"
                          #           },
                          #           {
                          #             "title":"Contact Info",
                          #             "type":"postback",
                          #             "payload":"CONTACT_INFO_PAYLOAD"
                          #           }
                          #         ]
                          #       },
                          #       {
                          #         "type":"web_url",
                          #         "title":"Latest News",
                          #         "url":"http://petershats.parseapp.com/hat-news",
                          #         "webview_height_ratio":"full"
                          #       }
                          #     ]
                          #   }
                          # ]
        })
        result = json.loads(requests.post(self.__urlProfile, params=self.__params, headers=self.__headers), data=data)
        return result["result"] == "sucess"

    def readMenu(self):
        params = {"access_token": Authentication.PAGE_ACCESS_TOKEN, "fields": "persistent_menu"}
        result = json.loads(requests.get(self.__urlProfile, params=params).text)
        return result

    def deleteMenu(self):
        data = json.dumps({"fields": ["persistent_menu"]})
        result = json.loads(requests.delete(self.__urlProfile, headers=self.__headers, params=self.__params, data=data).text)
        return result["result"] == "success"


    # ------ DOMAIN WHITELISTING ------
    # https://developers.facebook.com/docs/messenger-platform/messenger-profile/domain-whitelisting


    def setDomainWhiteList(self):
        data = json.dumps({"whitelisted_domains":Strings.WHITELIST})
        result = json.loads(
            requests.post(self.__urlProfile, headers=self.__headers, params=self.__params, data=data).text)
        return result["result"] == "success"

    def readDomainWhiteList(self):
        params = {"access_token": Authentication.PAGE_ACCESS_TOKEN, "fields": "whitelisted_domains"}
        result = json.loads(requests.get(self.__urlProfile, params=params).text)
        return result

    def deleteDomainWhiteList(self):
        data = json.dumps({"fields": ["whitelisted_domains"]})
        result = json.loads(requests.delete(self.__urlProfile, headers=self.__headers, params=self.__params, data=data).text)
        return result["result"] == "success"



    # ------ SETTING TARGET AUDIENCE ------
    # https://developers.facebook.com/docs/messenger-platform/messenger-profile/target-audience

    def setTargetAudience(self):
        #audience_type: all, custom or none
        #countries: Needs to be specified only when audience_type is custom.
        data = json.dumps({
                            "target_audience":{
                              "audience_type":"all"#,
                                # "countries":{
                                #     "whitelist":["US", "CA"] # or "blacklist"
                                # }
                            }
        })
        result = json.loads(requests.post(self.__urlProfile, headers=self.__headers, params=self.__params, data=data).text)
        return result["result"] == "success"

    def readTargetAudience(self):
        params = {"access_token": Authentication.PAGE_ACCESS_TOKEN, "fields": "target_audience"}
        result = json.loads(requests.get(self.__urlProfile, params=params).text)
        return result

    def deleteTargetAudience(self):
        data = json.dumps({"fields": ["target_audience"]})
        result = json.loads(
            requests.delete(self.__urlProfile, headers=self.__headers, params=self.__params, data=data).text)
        return result["result"] == "success"


    # ------ ACCOUNT LINKING URL ------
    # https://developers.facebook.com/docs/messenger-platform/messenger-profile/account-linking-url
    # https://developers.facebook.com/docs/messenger-platform/account-linking

    def setAccountLinkingURL(self):
        #TODO: Entender com funciona o uso do account linking url
        data = json.dumps({ "account_linking_url":Strings.ACCOUNT_LINKING_URL})
        result = json.loads(requests.post(self.__urlProfile, headers=self.__headers, params=self.__params, data=data).text)
        return result["result"] == "success"

    def readAccountLinkingURL(self):
        params = {"access_token": Authentication.PAGE_ACCESS_TOKEN, "fields": "account_linking_url"}
        result = json.loads(requests.get(self.__urlProfile, params=params).text)
        return result

    def deleteTargetAudience(self):
        data = json.dumps({"fields": ["account_linking_url"]})
        result = json.loads(
            requests.delete(self.__urlProfile, headers=self.__headers, params=self.__params, data=data).text)
        return result["result"] == "success"


    # ------ PAYMENTS SETTINGS ------
    # https://developers.facebook.com/docs/messenger-platform/messenger-profile/payment-settings

    def setPaymentPrivacyPolicy(self):
        data = json.dumps({ "payment_settings":{ "privacy_url":Strings.URL_PAYMENT_POLICY_PRIVACY } })
        result = json.loads(
            requests.post(self.__urlProfile, headers=self.__headers, params=self.__params, data=data).text)
        return result["result"] == "success"

    def setPublicKey(self):
        data = json.dumps({"payment_settings": {"public_key":Strings.PUBLIC_KEY}})
        result = json.loads(requests.post(self.__urlProfile, headers=self.__headers, params=self.__params, data=data).text)
        return result["result"] == "success"

    def  setPaymentTestUsers(self,client_id):
        data = json.dumps({"payment_settings": {"test_users": [client_id] }})
        result = json.loads(
            requests.post(self.__urlProfile, headers=self.__headers, params=self.__params, data=data).text)
        return result["result"] == "success"

    def readPaymentSettings(self):
        params = {"access_token": Authentication.PAGE_ACCESS_TOKEN, "fields": "payment_settings"}
        result = json.loads(requests.get(self.__urlProfile, params=params).text)
        return result

    def deletePaymentSettings(self):
        data = json.dumps({"fields": ["payment_settings"]})
        result = json.loads(
            requests.delete(self.__urlProfile, headers=self.__headers, params=self.__params, data=data).text)
        return result["result"] == "success"



