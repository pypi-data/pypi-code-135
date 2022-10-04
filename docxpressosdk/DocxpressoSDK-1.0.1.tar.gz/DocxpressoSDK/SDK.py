import hmac
import hashlib
import base64
import datetime
from msilib.schema import Control
from urllib.parse import quote
import json
import math
import random
import time
 
"""
 * Docxpresso SERVER SDK
 *    
 * @copyright  Copyright (c) 2017 No-nonsense Labs (http://www.nononsenselabs.com)
 * @license    MIT
 * @link       https://opensource.org/licenses/MIT
 * @version    5.0
 * @since      1.0
"""

class Utils:
    """
     * Construct
     *
     * @param array $options with the following keys and values
     *      'pKey' => (string) the private key of your Docxpresso SERVER 
     *       installation
     *      'docxpressoInstallation' => (string) the URL of your Docxpresso
     *      SERVER installation
     * 
     * @access public
    """
    def __init__(self, options):
        self._options = options


    """
     * Setter for options
     * @param array $options with the following keys and values
     *      'pKey' => (string) the private key of your Docxpresso SERVER 
     *       installation
     *      'docxpressoInstallation' => (string) the URL of your Docxpresso
     *      SERVER installation
     * 
     * @access public
     """
    def setOptions(self, options):
        _options = options
        return 
        
    
    """
    Checks the validity of an API key
 
      @param string $key the key you wish to validate
    @param string $data the string that was used to generate the key
    @param string $pKey the private key used to generate the hash
    @return boolean
    @access public
    """
    def apikey_control(self, key, data, pKey):
        byte_pkey = bytes(pKey, 'UTF-8')
        result = (hmac.new( byte_pkey, data.encode(), hashlib.sha1 )).hexdigest()
        if key == result: 
            return True
        else:
            return False


    """
    Encodes in base64 url safe
    
    @param string str
    @return string
    @access public
    """
    def base64_encode_url_safe(self, str):
        string_bytes = str.encode("ascii")
        base64_bytes = base64.b64encode(string_bytes)
        base64_string = base64_bytes.decode("ascii")
        return base64_string.replace('+','-',1000).replace('/','_',1000).replace('=',',',1000)
     

    """
     Decodes base64 url safe
     
    @param string str
    @return string 
    @access public
    """ 
    def base64_decode_url_safe(self, str):
    
        str = str.replace('-','+',1000).replace('_','/',1000).replace(',','=',1000)
        string_bytes = str.encode("ascii")
        base64_bytes = base64.b64decode(string_bytes)
        base64_string = base64_bytes.decode("ascii")
        return base64_string


    """
     * Generates a one time link to preview a document in the associated
     * Docxpresso SERVER interface
     * 
     * NOTE: if data is loaded from various sources it will be loaded with the 
     * folllowing priority: varData, requestDataURI, token
     * 
     * @param array $data with the following keys and values
     *      'template' => (int) the id of the requested document template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'token' => (string) a unique identifier of a previous use. If given
     *       the data associated with the token will be preloaded into 
     *       the document.
     *      'identifier' => (string) optional var name that we may pass to help 
     *       identify that particular usage. Default value is an empty string 
     *      'reference' => (string) an optional string we may pass to help 
     *       identify that particular usage. Default value is an empty string
     *      'expires' => (integer) the number of seconds after which the link
     *       is no longer valid. 
     *      'custom' => (string) an optional string we may pass to add external
     *       additional info to the template
     *      'form' => (boolean) if true Docxpresso will serve a web form rather
     *       than an interactive document. Default value is false.
     *      'format' => (string) the requested document output format. The
     *       possible values include odt, pdf, doc, docx and rtf. If not given
     *       the available formats will be taken from the template settings.
     *      'enduserid' => (string) a value that will help us later to identify
     *       the user that requested the document. Default value is an empty 
     *       string.
     *      'email' => (string) the email of the user to send additional
     *       notifications. 
     *      'requestConfigURI' => (string) the URL where Docxpresso should fetch
     *       external configuration adjustments.
     *      'requestDataURI' => (string) the URL where Docxpresso should fetch
     *       external data. Default value is an empty string.
     *      'requestExternalCSS' => (string) the URL where Docxpresso should
     *       fetch for some external CSS file.
     *      'requestExternalJS' => (string) the URL where Docxpresso should
     *       fetch for some external JS file.
     *      'responseDataURI' => (string) the URL where Docxpresso should
     *       forward the user data. Default value is an empty string.
     *      'processingDataURI' => (string) the URL where Docxpresso should
     *       postprocess doc data. Default value is an empty string.
     *      'responseURL' => (string) the URL where Docxpresso should redirect
     *       the end user after saving the data. Default value is an empty 
     *       string. 
     *      'documentName' => (string) the name we want to give to the generated
     *       document. Default value is empty and in that case Docxpresso
     *       will use the default template name. 
     *       string.
     *      'domain' => (string) the URL doing the request. Default value is an 
     *       empty string.
     *      'prefix' => (string) a prefix that will limit enduser edition to
     *       only the field variables that start by that prefix. You can use
     *       a comma separated list to select more than one prefix. Default value 
     *       is an empty string.
     *      'editableVars' => (string) a comma separated list of var names
     *       to restrict the edition to that set. Default value is an empty 
     *       string.
     *      'blockVars' => (string) a comma separated list of var names
     *       which edition is expicitly blocked. Default value is an empty 
     *       string.
     *      'enforceValidation' => (boolean) if true the user will not be able
     *       to send data until all variable fields are validated. Default value
     *       is false.
     *      'language' => (string) if set will change the default interface
     *       language. Currently available values are: default, en, es
     *      'GDPR' => (boolean) if true the end user will be prompted to check
     *       the privacy policy (it only applies if it is also globally defined)
     *      'phone' => (string) with standard international format +12121112222.
     *       If given the end user will be first prompted to introduce an OTP
     *       sent to that phone.
     *      'OTPmessage' => (string) this only applies if we use a phone to
     *       request an OTP
     *      'varData' => additional JSON data we would like to preload into the 
     *       document
     *      'continueLink' => (boolean) if true the end user will be prompted
     *       to introduce an email where he can continue later the edition
     *      'continueLinkEmail' => if continueLink is set to true and this 
     *       option is given it will be shown as the default email to receive
     *       the continue link.
     *      'blockDocument' => (int) if equals "1" the end user will be asked if
     *       the document should be blocked from further edition, else if equals
     *       "2" the document wil be automatically blocked after first use and 
     *       finally if it equals "3" the document will be automatically blocked
     *       only if the end user is not a registered backoffice user.
     *      'history' => (boolean) if true and there is a token (or history data
     *       is provided from external sources) the user will be able to
     *       visualize the edition history of the document.
     *      'keepAlive' => (boolean) if true the generated link is alived and
     *       allows for multiple editions of the same document.
     *      'trackID' => (string) if given it will be used whenever the 
     *       keepAlive is set to true, otherwise it will be autogenerated.
     *      'loadContactData' => (integer) id of the contact whose data we want
     *       to load into the template.
     *      'requestVars' => (array) list of variables that should be sent in
     *       the query parameter of the responseURL
     *      'plugin' => (boolean) if true the petition may directly come from
     *       a plugin user so further security checks may be carried out to test
     *       for data coherence and permissions.
     *      'enableRejection' => (boolean) if true the user will be offered a
     *       button to directly 'reject' the document wuithout fulfilling it.
     *      'livePreview' => (boolean) this property only applies to web forms, 
     *       if true a live preview of the generated document will be offered.
     *      'client' => (integer) cliend id. Only for multi tenant instances. 
     *      'tabDisplay' => (string) if "full" the tabs will be forced to be
     *       fully displayed even if there are more than 5. default value is 
     *       "auto".
     * @return string
     * @access public
     """
    def previewDocument(self, data):
         
        if (not(self.empty(data, 'phone'))):
            url = self._options['docxpressoInstallation'] + '/tracking/OTP/request_OTP/' + str(data['template'])
        elif not(self.empty(data,'form')) and data.form:
            url = self._options['docxpressoInstallation'] + '/documents/previewForm/' + str(data['template'])
        else:
            url = self._options['docxpressoInstallation'] + '/documents/preview/' + str(data['template'])
        
        options = {}
        
        if not(self.empty(data,'form')) and data.form:
            options['display'] = 'form'
        else :
            options['display'] = 'document'
        
        if not(self.empty(data,'phone')):
            options['phone'] = data['phone']
            options['action'] = 'preview'
        
        if not(self.empty(data,'OTPmessage')):
            options['OTPmessage'] = quote(data['OTPmessage'])
        
        if (self.isset(data,'token')) :
            options['token'] = data['token']
        
        if (self.isset(data,'format')) :
            options['forceFormat'] = data['format']
        
        if (self.isset(data,'enduserid')) :
            options['enduserid'] = data['enduserid']
        
        if (self.isset(data,'email')) :
            options['email'] = data['email']
        
        #notice that if continueLink is given the enduserid will be overwritten
        if (self.isset(data,'continueLink') and data.continueLink) :
            options['access'] = 'authenticated'
            options['enduserid'] = self._generateOTP()
        
        if (self.isset(data,'continueLinkEmail')) :
            #notice that this will overwrite the email parameter if given
            options['email'] = data['continueLinkEmail']
        
        if (self.isset(data,'identifier')) :
            options['identifier'] = data['identifier']
        
        if not(self.empty(data,'client')) :
            options['client'] = data['client']
        
        if (self.isset(data,'expires')) :
            options['expires'] = data['expires']
        
        if (self.isset(data,'reference')) :
            options['reference'] = data['reference']
        
        if (self.isset(data,'custom')) :
            options['custom'] = data['custom']
        
        if not(self.empty(data,'requestConfigURI')) :
            dURI = {}
            dURI['URL'] = data['requestConfigURI']
            options['requestConfigURI'] = json.dumps(dURI, separators=(',', ':'))
        
        if not(self.empty(data,'requestDataURI')) :
            dURI = {}
            dURI['URL'] = data['requestDataURI']
            dURI['requestData'] = 'preview'
            options['requestDataURI'] = json.dumps(dURI, separators=(',', ':'))    
        
        if (self.isset(data,'requestExternalJS')) :
            options['requestExternalJS'] = data['requestExternalJS']
        
        if (self.isset(data,'requestExternalCSS')) :
            options['requestExternalCSS'] = data['requestExternalCSS']
        
        if not(self.empty(data,'responseDataURI')) :
            options['responseDataURI'] = data['responseDataURI']
        
        if not(self.empty(data,'processingDataURI')) :
            options['processingDataURI'] = data['processingDataURI']
        
        if not(self.empty(data,'responseURL')) :
            options['responseURL'] = data['responseURL']
        
        if not(self.empty(data,'documentName')) :
            options['documentName'] = data['documentName']
        
        if not(self.empty(data,'domain')) :
            options['domain'] = data['domain']
        
        if not(self.empty(data,'prefix')) :
            options['prefix'] = data['prefix']
        
        if not(self.empty(data,'editableVars')) :
            options['editableVars'] = data['editableVars']
        
        if not(self.empty(data,'blockVars')) :
            options['blockVars'] = data['blockVars']
        
        if not(self.empty(data,'enforceValidation')) :
            options['enforceValidation'] = True
        
        if not(self.empty(data,'GDPR')) :
            options['GDPR'] = True
        
        if not(self.empty(data,'livePreview')) :
            options['viewDoc'] = True
        
        if not(self.empty(data,'language')) :
            options['locale'] = data['language']
        
        if (self.isset(data,'varData')) :
            options['data'] = data['varData']
        
        if not(self.empty(data,'history')) :
            options['history'] = 1
        
        if not(self.empty(data,'blockDocument')) :
            options['blockDocument'] = data['blockDocument']
        
        if not(self.empty(data,'keepAlive')) :
            options['keepAlive'] = 1
            #we should also generate a trackID to be able to keep track
            #of consequent editions
            if not(self.empty(data,'trackID')):
                options['trackID'] = data['trackID']
            else :
                preseed = self.generate_uniqid()+ data['template'] + self.generate_uniqid()
                salt = 'd2g6IOP(U(&Â§)%UÂ§VUIPU(HN%V/Â§Â§URerjh0Ã¼rfqw4zoÃ¶qe54gÃŸ0Ã¤Q"LOU$3w er'
                prehash = hashlib.sha1(str(preseed).encode('utf-8')).hexdigest()
                
                trackID = hashlib.md5(str(salt + prehash).encode('utf-8')).hexdigest()
                options.trackID = trackID           
        
        if (not(self.empty(data,'loadContactData')) and isinstance(data['loadContactData'], int) and (data['loadContactData'] > 0)):
            options['preloadDXData'] = 1
            options['DXData'] = {}
            options['DXData']['type'] = "contact"
            options['DXData']['contact'] = data['loadContactData']  
        
        if (self.isset(data,'requestVars') and len(data['requestVars']) > 0) :
            options['requestVars'] = ','.join(data['requestVars'])
        
        if not(self.empty(data,'plugin')) :
            options['plugin'] = 1
        
        if not(self.empty(data,'enableRejection')) :
            options['enableRejection'] = 1
        
        if not(self.empty(data,'tabDisplay')) :
            options['tabDisplay'] = data['tabDisplay']

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
        
        return self._returnLink(url, data['template'], opt) 


    """
     * Generates a one time link to validate a document in the associated
     * Docxpresso SERVER interface
     * 
     * @param array $data with the following keys and values
     *      'template' => (int) the id of the requested document template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'token' => (string) a unique identifier of a previous use. This 
     *       value is complusory and must correspond to a valid usage token.
     *      'requestDataURI' => (string) the URL where Docxpresso should fetch
     *       external data. Default value is an empty string.
     *      'varData' => additional JSON data we would like to preload into the 
     *       document
     *      'name' => (string) the name of the user that wll validate the 
     *       document.
     *      'email' => (string) the email of the user that wll validate the 
     *       document.
     *      'phone' => (string) with standard international format +12121112222.
     *       If given the end user will be first prompted to introduce an OTP
     *       sent to that phone. If the value is set as "request" the user will 
     *       be prompted to introduce his phone in the validation interface.
     *      'OTPmessage' => (string) this only applies if we use a phone to
     *       request an OTP
     *      'custom' => (string) an optional string we may pass to add external
     *       additional info to the validation process.
     *      'language' => (string) if set will change the default interface
     *       language. Currently available values are: default, en, es.
     *      'responseDataURI' => (string) the URL where Docxpresso should
     *       forward the user data. Default value is an empty string.
     *      'responseURL' => (string) the URL where Docxpresso should redirect
     *       the end user after validating the data. Default value is an empty 
     *       string.
     *      
     * @return string
     * @access public
     """
    def validateDocument(self, data):
    
        url = self._options['docxpressoInstallation'] + '/documents/validate/preview/'
        url += str(data['template']) + '/' + str(data['token'])
        options = {}
        if (self.isset(data,'name')) :
            options['name'] = data['name']
        
        if (self.isset(data,'email')) :
            options['email'] = data['email']
        
        if not(self.empty(data,'phone')):
            options['phone'] = data['phone']
        
        if not(self.empty(data,'OTPmessage')):
            options['OTPmessage'] = quote(data['OTPmessage'])
        
        if (self.isset(data,'custom')) :
            options['custom'] = data['custom']
        
        if (self.isset(data,'responseURL')) :
            options['responseURL'] = data['responseURL']
        
        if not(self.empty(data,'responseDataURI')) :
            options['responseDataURI'] = data['responseDataURI']
        
        if not(self.empty(data,'requestDataURI')) :
            dURI = {}
            dURI['URL'] = data['requestDataURI']
            dURI['requestData'] = 'validate'
            options['requestDataURI'] = json.dumps(dURI, separators=(',', ':'))
        
        if (self.isset(data,'varData')) :
            options['data'] = data['varData']
        
        if not(self.empty(data,'language')) :
            options['locale'] = data['language']
        
        
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
        """
        //in this case we need to concatenate id and token so the apikey
        //can not be reused for methods that allowed to use twice the
        //apikey
        """
        id = str(data['template']) + str(data['token'])
        return self._returnLink(url, id, opt)   
    

    """
     * Generates a one time link to preview a document in the associated
     * Docxpresso SERVER interface and sends it by email to the end user
     * 
     * NOTE: if data is loaded from various sources it will be loaded with the 
     * folllowing priority: varData, requestDataURI, token
     * 
     * @param array $data with the following keys and values
     *      'template' => (int) the id of the requested document template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'token' => (string) a unique identifier of a previous use. If given
     *       the data associated with the token will be preloaded into 
     *       the document.
     *      'identifier' => (string) optional var name that we may pass to help 
     *       identify that particular usage. Default value is an empty string 
     *      'reference' => (string) an optional string we may pass to help 
     *       identify that particular usage. Default value is an empty string
     *      'expires' => (integer) the number of seconds after which the link
     *       is no longer valid. 
     *      'custom' => (string) an optional string we may pass to add external
     *       additional info to the template
     *      'form' => (boolean) if true Docxpresso will serve a web form rather
     *       than an interactive document. Default value is false.
     *      'format' => (string) the requested document output format. The
     *       possible values include odt, pdf, doc, docx and rtf. If not given
     *       the available formats will be taken from the template settings.
     *      'enduserid' => (string) a value that will help us later to identify
     *       the user that requested the document. Default value is an empty 
     *       string.
     *      'email' => (string) the email of the user to send additional
     *       notifications. 
     *      'requestConfigURI' => (string) the URL where Docxpresso should fetch
     *       external configuration adjustments.
     *      'requestDataURI' => (string) the URL where Docxpresso should fetch
     *       external data. Default value is an empty string.
     *      'requestExternalCSS' => (string) the URL where Docxpresso should
     *       fetch for some external CSS file.
     *      'requestExternalJS' => (string) the URL where Docxpresso should
     *       fetch for some external JS file.
     *      'responseDataURI' => (string) the URL where Docxpresso should
     *       forward the user data. Default value is an empty string.
     *      'processingDataURI' => (string) the URL where Docxpresso should
     *       postprocess doc data. Default value is an empty string.
     *      'responseURL' => (string) the URL where Docxpresso should redirect
     *       the end user after saving the data. Default value is an empty 
     *       string. 
     *      'documentName' => (string) the name we want to give to the generated
     *       document. Default value is empty and in that case Docxpresso
     *       will use the default template name. 
     *       string.
     *      'domain' => (string) the URL doing the request. Default value is an 
     *       empty string.
     *      'prefix' => (string) a prefix that will limit enduser edition to
     *       only the field variables that start by that prefix. You can use
     *       a comma separated list to select more than one prefix. Default value 
     *       is an empty string.
     *      'editableVars' => (string) a comma separated list of var names
     *       to restrict the edition to that set. Default value is an empty 
     *       string.
     *      'blockVars' => (string) a comma separated list of var names
     *       which edition is expicitly blocked. Default value is an empty 
     *       string.
     *      'enforceValidation' => (boolean) if true the user will not be able
     *       to send data until all variable fields are validated. Default value
     *       is false.
     *      'language' => (string) if set will change the default interface
     *       language. Currently available values are: default, en, es
     *      'GDPR' => (boolean) if true the end user will be prompted to check
     *       the privacy policy (it only applies if it is also globally defined)
     *      'phone' => (string) with standard international format +12121112222.
     *       If given the end user will be first prompted to introduce an OTP
     *       sent to that phone.
     *      'OTPmessage' => (string) this only applies if we use a phone to
     *       request an OTP
     *      'varData' => additional JSON data we would like to preload into the 
     *       document
     *      'continueLink' => (boolean) if true the end user will be prompted
     *       to introduce an email where he can continue later the edition
     *      'continueLinkEmail' => if continueLink is set to true and this 
     *       option is given it will be shown as the default email to receive
     *       the continue link.
     *      'blockDocument' => (boolean) if true the end user will be asked if
     *       the document should be blocked from further edition.
     *      'history' => (boolean) if true and there is a token (or history data
     *       is provided from external sources) the user will be able to
     *       visualize the edition history of the document.
     *      'keepAlive' => (boolean) if true the generated link is alived and
     *       allows for multiple editions of the same document.
     *      'trackID' => (string) if given it will be used whenever the 
     *       keepAlive is set to true, otherwise it will be autogenerated.
     *      'loadContactData' => (integer) id of the contact whose data we want
     *       to load into the template.
     *      'requestVars' => (array) list of variables that should be sent in
     *       the query parameter of the responseURL
     *      'plugin' => (boolean) if true the petition may directly come from
     *       a plugin user so further security checks may be carried out to test
     *       for data coherence and permissions.
     *      'enableRejection' => (boolean) if true the user will be offered a
     *       button to directly 'reject' the document wuithout fulfilling it.
     *      'livePreview' => (boolean) this property only applies to web forms, 
     *       if true a live preview of the generated document will be offered.
     *      'client' => (integer) cliend id. Only for multi tenant instances.
     * @param array $mailer with the following keys and values
     *      'email' => (string) the email address where to send the edition link
     *      'logo' => (string) URL where to fetch the logo. If not given the 
     *       default Docxpresso instance logo will be used
     *      'subject' => (string) email subject. If not given the template title
     *       will be used
     *      'body' => (string) HTML text. If not given the template description
     *       will be used.
     *      'callToAction' => (string) text of the link button. If not given
     *       the default text will be used.
     *      'emailTemplate' => (string) path to the required email template. 
     *       If not given the default template will be used.
     *      'footer' => (string) HTML text. If not given the default footer
     *       will be used.
     * 
     * @return string
     * @access public
     """
    def sendEditLinkByEmail(self, data, mailer):
    
        link = self.previewDocument(data)
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/send_email_edit/' + str(data['template'])
        options = {}
        options['link'] = link
        if (self.isset(mailer,'email')) :
            options['email'] = mailer['email']
        
        if (self.isset(mailer,'logo')) :
            options['logo'] = mailer['logo']
        
        if not(self.empty(mailer,'subject')):
            options['subject'] = mailer['subject']
        
        if not(self.empty(mailer,'body')):
            options['body'] = mailer['body']
        
        if (self.isset(mailer,'callToAction')) :
            options['callToAction'] = mailer['callToAction']
        
        if (self.isset(mailer,'emailTemplate')) :
            options['emailTemplate'] = mailer['emailTemplate']
        
        if (self.isset(mailer,'footer')) :
            options['footer'] = mailer['footer']
        

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
        return self._returnLink(url, data['template'], opt)
    

    """
     * Returns a link to download all document validations in JSON(P)  
     * format  for a given template id from the associated Docxpresso 
     * SERVER installation
     * 
     * @param array $data with the following keys and values
     *      'id' => (int) the id of the template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'status' => (boolean) if true only acepted documents will be listed
     *       and if false only rejected documents will be listed. Default value
     *       is empty
     *      'enduserid' => (string) the end user id of a particular revision.
     *       Default value is empty.
     *      'period' => (string) if given will overwrite the given startDate and
     *       enddate parameters. The possible values are: today, 
     *       1week (last week), 1month (last month), 3month (last quarter),
     *       year (last year). The default value is empty
     *      'startDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened after it. Default value is an empty 
     *       string.
     *      'endDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened before it. Default value is an empty 
     *       string.
     *      'firstResult' => (int) query offset. Default value is 0; 
     *      'maxResults' => (int) maximum number of results. Beware that
     *       each installation may have its own limits to this number
     *      (usually 100)
     *       Default value is empty and Docxpresso default will be used.
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
     """
    def validationsByTemplate(self, data, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/validations_by_template/' + str(data['id'])
		
        if (callback != '' and callback != None) :
            url += '/' + callback
        
        options = {}
        if (self.isset(data,'status') and data['status']):
            options['status'] = 1
        elif (self.isset(data,'status') and not(data['status'])) :
            options['status'] = 0
        else :
            options['status'] = 2
        
        if not(self.empty(data,'enduserid')) :
            options['enduserid'] = data['enduserid']
        
        #dates must be in the format 2016-01-30
        if not(self.empty(data,'startDate')) :
            options['startDate'] = data['startDate']
        
        if not(self.empty(data,'endDate')) :
            options['endDate'] = data['endDate']
        
        if not(self.empty(data,'period')) :
            options['period'] = data['period']
        
        if not(self.empty(data,'firstResult')) :
            options['firstResult'] = data['firstResult']
        
        if not(self.empty(data,'maxResults')) :
            options['maxResults'] = data['maxResults']
        
        if not(self.empty(data,'sort')) :
            options['sort'] = data['sort']
        
        if not(self.empty(data,'order')) :
            options['order'] = data['order']
        
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
		
        return self._returnLink(url, data['id'], opt)


    """
     * Generates a one time link to simply view a document within the
     * Docxpresso interface with no action associated
     * 
     * @param array $data with the following keys and values
     *      'template' => (int) the id of the requested document template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'token' => (string) a unique identifier of a previous use. This 
     *       value must correspond to a valid usage token.
     *      'requestDataURI' => (string) the URL where Docxpresso should fetch
     *       external data. Default value is an empty string.
     *      'varData' => the JSON data we would like to use to generate the 
     *       document.
     *      'language' => (string) if set will change the default interface
     *       language. Currently available values are: default, en, es.
     *      'toolBar' => (boolean) if false the fixed bar at the top will be 
     *       removed.
     *      'permanent' => (boolean) if set the link will never expire. Default 
     *       value is false.
     *      'history' => (boolean) if true the user will be able to
     *       visualize the edition history of the document.
     *      
     * @return string
     * @access public
     """
    def viewDocument(self, data):
        
        if (self.empty(data,'token')):
            data['token'] = 0
        
        url = str(self._options['docxpressoInstallation']) + '/documents/validate/view/'
        url += str(data['template']) + '/' + str(data['token'])
        options = {}
        if not(self.empty(data,'requestDataURI')) :
            dURI = {}
            dURI['URL'] = data['requestDataURI']
            dURI['requestData'] = 'view'
            options['requestDataURI'] = json.dumps(dURI, separators=(',', ':'))
        
        if (self.isset(data,'varData')) :
            options['data'] = data['varData']
        
        if not(self.empty(data,'language')) :
            options['locale'] = data['language']
        
        if (self.isset(data,'toolBar')) :
            options['toolBar'] = data['toolBar']
        
        if (self.isset(data,'permanent')) :
            options['permanent'] = data['permanent']
        
        if not(self.empty(data,'history')) :
            options['history'] = 1
        
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
        """
        //in this case we need to concatenate id and token so the apikey
        //can not be reused for methods that allowed to use twice the
        //apikey
        """
        id = str(data['template']) + str(data['token']) + 'view'
        return self._returnLink(url, id, opt)  
    

    """
     * Generates a one time link to simply view a document history within the
     * Docxpresso interface with no action associated
     * 
     * @param array $data with the following keys and values
     *      'template' => (int) the id of the requested document template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'token' => (string) a unique identifier of a previous use. This 
     *       value must correspond to a valid usage token.
     *      'requestDataURI' => (string) the URL where Docxpresso should fetch
     *       external data with history data. Default value is an empty string.
     *       if given it will override the token.
     *      'varData' => the JSON data we would like to use to generate the 
     *       history associated with that document. If given will override the
     *       token and requestDataURI.
     *      'language' => (string) if set will change the default interface
     *       language. Currently available values are: default, en, es.
     *      
     * @return string
     * @access public
     """
    def viewHistoryDocument(self, data):
     
        if (self.empty(data,'token')):
            data['token'] = 0
        
        url = str(self._options['docxpressoInstallation']) + '/documents/history/view/'
        url += str(data['template']) + '/' + str(data['token'])
        options = {}
        if not(self.empty(data,'requestDataURI')) :
            dURI = {}
            dURI['URL'] = data['requestDataURI']
            dURI['requestData'] = 'preview'
            options['requestDataURI'] = json.dumps(dURI, separators=(',', ':'))
        
        if (self.isset(data,'varData')) :
            options['data'] = data['varData']
        
        if not(self.empty(data,'language')) :
            options['locale'] = data['language']
        
        
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
        """
        //in this case we need to concatenate id and token so the apikey
        //can not be reused for methods that allowed to use twice the
        //apikey
        """
        id = str(data['template']) + str(data['token']) + 'view'
        return self._returnLink(url, id, opt);    


    """
     * Generates a one time link to regenerate a "full· document package" in zip
     * format (document + attachments) from the associated
     * Docxpresso SERVER installation
     * 
     * @param array $data with the following keys and values
     *      'id' => (int) the id of the corresponding template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'token' => (string) the token of the requested usage.
     *      'identifier' => (string) if given the token will be ignored and
     *       the returned document will be the last document retrieved with that
     *       identifier.
     *      'onlyDocument' => (boolean) if true only downloads the main document
     *       ignoring any potential attachment. Default value false.
     *      'documentName' => (string) the name we want to give to the generated
     *       document (it should include the extensions: .odt, .pdf, .doc, 
     *       .doc(legacy), .docx or .rtf). The default values is document.odt
     * 
     * @return string
     * @access public
     """
    def regenerateDocument(self, data):
    
        url = str(self._options['docxpressoInstallation']) + '/documents/regenerateDocument/' + str(data['id'])
        options = {}

        if not(self.empty(data,'identifier')):
            options['identifier'] = data['identifier']
        else :
            options['token'] = data['token']
        
        if (self.isset(data,'onlyDocument')):
            options['onlyDocument'] = data['onlyDocument']
        
        if (self.isset(data,'documentName')):
            options['documentName'] = data['documentName']
        
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
       
        return self._returnLink(url, data['id'], opt)


    """
     * Generates a one time link to generate a document in the associated
     * Docxpresso SERVER interface
     * 
     * NOTE: if data is loaded from various sources it will be loaded with the 
     * folllowing priority: varData, requestDataURI, token
     * 
     * @param array $data with the following keys and values
     *      'template' => (int) the id of the requested document template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'identifier' => (string) optional var name that we may pass to help 
     *       identify that particular usage. Default value is an empty string 
     *      'reference' => (string) an optional string we may pass to help 
     *       identify that particular usage. Default value is an empty string
     *      'requestDataURI' => (string) the URL where Docxpresso should fetch
     *       external data. Default value is an empty string.
     *      'documentName' => (string) the name we want to give to the generated
     *       document (it should include the extensions: .odt, .pdf, .doc, 
     *       .doc(legacy), .docx or .rtf). The default value is document.odt
     *      'varData' => the JSON data we would like to use to generate the 
     *       document.
     *      'token' => (string) a unique identifier of a previous use. If given
     *       the data associated with the token will be preloaded into 
     *       the document.
     *      'display' => (string) it can be 'document' (default) or 'form'. 
     *       This is only used for the generation of continue links
     *      'response' => (string) it can be 'download'(default) if the document
     *       is to be directly downloadable from the browser or 'json' if we want
     *       to get the document as base64 encoded together with the usage id
     *       and token
     *      'callback' => it only spplies to json responses and sets the name
     *       of the callback function for JSONP responses.
     *      'client' => (integer) cliend id. Only for multi tenant instances. 
     * @return string
     * @access public
     """
    def requestDocument(self, data):
      
        url = str(self._options['docxpressoInstallation']) + '/documents/requestDocument/' + str(data['template'])
	
        options = {}
        if (self.isset(data,'documentName')) :
            options['name'] = data['documentName']
        else :
            options['name'] = 'document.odt'
        
        if (self.isset(data,'varData')) :
            options['data'] = data['varData']
        else :
            options['data'] = '{}'
        
        if (self.isset(data,'display')) :
            options['display'] = data['display']
        else :
            options['display'] = 'document'
        
        if not(self.empty(data,'requestDataURI')) :
            dURI = {}
            dURI['URL'] = data['requestDataURI']
            dURI['requestData'] = 'request'
            options['requestDataURI'] = json.dumps(dURI, separators=(',', ':'))
        
        if (self.isset(data,'token')) :
            options['token'] = data['token']
        
        if (self.isset(data,'identifier')) :
            options['identifier'] = data['identifier']
        
        if not(self.empty(data,'client')) :
            options['client'] = data['client']
        
        if (self.isset(data,'reference')) :
            options['reference'] = data['reference']
        
        if (self.isset(data,'response')) :
            options['response'] = data['response']
        

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
        
        return self._returnLink(url, data['template'], opt)
    

    """
     * Generates a one time link to sign a document generated with Docxpresso
     * 
     * @param array $data $data with the following keys and values
     *      'usageId' => (int) the id of the corresponding usage.
     *       This value is compulsory and must correspond to a valid document
     *      'token' => (string) the token of the given usage for further
     *       security. 
     *      'provider' => (string) it can be vidSigner, Lleida.net or NodalBlock
     *      'signers' => (array) an array of arrays where the second array 
     *       includes the following key and values (some may be optional
     *       depending on the provider and how the signature is parametrized):
     *          'name': (string) signer's name
     *          'id': (string) signer's id
     *          'email': (string) signer's email
     *          'phone': (string) signer's phone
     *       
     * @return string
     * @access public
    """
    def requestSignature(self, data):
        #TO BE DONE
        
     """
    Returns a link to download all document revisions in JSON(P)  
    format  for a given template id from the associated Docxpresso 
    SERVER installation
    
    @param array $data with the following keys and values
     *      'id' => (int) the id of the template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'status' => (boolean) if true only acepted documents will be listed
     *       and if false only rejected documents will be listed. Default value
     *       is empty
     *      'enduserid' => (string) the end user id of a particular revision.
     *       Default value is empty.
     *      'period' => (string) if given will overwrite the given startDate and
     *       enddate parameters. The possible values are: today, 
     *       1week (last week), 1month (last month), 3month (last quarter),
     *       year (last year). The default value is empty
     *      'startDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened after it. Default value is an empty 
     *       string.
     *      'endDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened before it. Default value is an empty 
     *       string.
     *      'firstResult' => (int) query offset. Default value is 0; 
     *      'maxResults' => (int) maximum number of results. Beware that
     *       each installation may have its own limits to this number
     *      (usually 100)
     *       Default value is empty and Docxpresso default will be used.
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
     """
    def revisionsByTemplate(self, data, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/revisions_by_template/' + str(data['id'])
		
        if (callback != '' and callback != None) :
                url += '/' + str(callback)
        

        #we build and options object with the search filters
        options = {}
        if (self.isset(data,'status') and data['status']) :
            options['status'] = 1
        elif (self.isset(data,'status') and not(data['status'])) :
            options['status'] = 0
        else :
            options['status'] = 2
        
        if not(self.empty(data,'enduserid')) :
            options['enduserid'] = data['enduserid']
        
        #dates must be in the format 2016-01-30
        if not(self.empty(data,'startDate')) :
            options['startDate'] = data['startDate']
        
        if not(self.empty(data,'endDate')) :
            options['endDate'] = data['endDate']
        
        if not(self.empty(data,'period')) :
            options['period'] = data['period']
        
        if not(self.empty(data,'firstResult')) :
            options['firstResult'] = data['firstResult']
        
        if not(self.empty(data,'maxResults')) :
            options['maxResults'] = data['maxResults']
        
        if not(self.empty(data,'sort')) :
            options['sort'] = data['sort']
        
        if not(self.empty(data,'order')) :
            options['order'] = data['order']
        

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
		
        return self._returnLink(url, data['id'], opt)
    

    """
     * Generates a one time link to download an attachment from the associated
     * Docxpresso SERVER installation
     * 
     * @param array $data $data with the following keys and values
     *      'usageId' => (int) the id of the corresponding usage.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'name' => (string) the name of the attachment file we want to
     *       download. It should correspond to the name given in the Docxpresso
     *       SERVER processing interface.
     *      'token' => (string) the token of the given usage for further
     *       security. 
     * @return string
     * @access public
    """
    def downloadAttachment(self, data):
    
        url = str(self._options['docxpressoInstallation']) + '/documents/getAttachment/' + str(data['usageId'])

        uniqid = self.generate_uniqid()
        timestamp =  int(time.time())

        options = {}
        options['name'] = data['name']
        options['token'] = data['token']
	
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
      
        return self._returnLink(url, data['usageId'], opt);     
    

    """
     * Generates a one time link to download a "full· document package" in zip
     * format (document + attachments) from the associated
     * Docxpresso SERVER installation
     * 
     * @param array $data $data with the following keys and values
     *      'id' => (int) the id of the corresponding template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'token' => (string) the token of the requested usage.
     *      'identifier' => (string) if given the token will be ignored and
     *       the returned docuemnt will be the last document retrieved with that
     *       identifier.
     *      'onlyDocument' => (boolean) if true only downloads the main document
     *       ignoring any potential attachment. Default value false.
     *       'plugin' => (boolean) if true the petition may directly come from
     *       a plugin user so further security checks may be carried out to test
     *       for data coherence and permissions.
     * 
     * @return string
     * @access public
    """
    def downloadDocument(self, data):
    
        url = str(self._options['docxpressoInstallation']) + '/documents/getFullDocumentation/' + str(data['id'])

        options = {}
        if not(self.empty(data,'identifier')):
            options['identifier'] = data['identifier']
        else :
            options['token'] = data['token']
        
        if (self.isset(data,'onlyDocument')):
            options['onlyDocument'] = data['onlyDocument']
        
        if not(self.empty(data,'plugin')) :
            options['plugin'] = 1
        
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
       
        return self._returnLink(url, data['id'], opt)
    

    """
     * Generates a one time link to get a JSON with all info associated with
     * a forwarded document including the document base64 encoded(it may be
     * a zip if the document has attachments) from the associated
     * Docxpresso SERVER installation
     * 
     * @param array $data $data with the following keys and values
     *      'id' => (int) the id of the corresponding forwarded document
     *      'processed' => (int) if given will set the processed flag this
     *      value. For example you may set its value to 1 in order to restrict
     *      future searches. 
     * @return string
     * @access public
     """
    def fetchForwardedDocument(self, data):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/fetch_forwarded_document/' + str(data['id'])
    
        options = {}
        if (self.isset(data,'processed')):
            options['processed'] = data['processed']
        
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
       
        return self._returnLink(url, data['id'], opt)
    

    """
     * Generates a one time link to get all annex document data: thumbnail, 
     * base64 encoded template odt file, etcetera.
     * 
     * @param integer $token the token of the requested annex
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
     """
    def getAnnexData(self, token, callback = ''):
    
        url = self._options['docxpressoInstallation'] + '/RESTservices/predefined/get_annex/' + token

        if (callback != '' and callback != None) :
            url += '/' + callback
        
		
        return self._returnLink(url)
    

    """
     * Generates a one time link to get all document template data: Docxpresso
     *  data, thumbnail, base64 encoded template odt file, etcetera.
     * 
     * @param integer $id the id of the required template
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
     """
    def getTemplateData(self, id, callback = ''):
      
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/get_template/' + str(id)

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
		
        return self._returnLink(url, id)
    

    """
     * Generates a one time link to get just a template thumbnail
     * 
     * @param integer $id the id of the required template
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
     """
    def getTemplateThumbnail(self, id, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/get_thumbnail/' + str(id)

        if (callback != '' and callback != None) :
            url += '/' + callback
        
		
        return self._returnLink(url, id)
    

    """
     * Generates a one time link to get the signatures parametrization data
     * from the template
     * 
     * @param integer $id the id of the required template
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def getTemplateSignatureData(self, id, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/get_template_signature_data/' + str(id)

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
		
        return self._returnLink(url, id)
    

    """
     * Get current usage for administrative purposes
     * 
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return array
     * @access public
    """
    def getUsageCurrent(self, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/get_usage_current'

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
		
        return self._returnLink(url)
    



    """
     * Get usage history by year/month for administrative purposes
     * 
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def getUsageHistory(self, callback = ''):
     
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/get_usage_history'

        if (callback != '' and callback != None) :
            url += '/' + callback
        
		
        return self._returnLink(url)
    

    """
     * Modifies the template configuration: variables and groups. 
     * WARNING: beware that in order to modify the group properties you need
     * to know the group ids that can be retrieved with the getTemplateData
     * method or generated as follows: in order to generate the id one need to
     * know the name of all variables inclued in the group and generate the
     * md5 hash obtained from concatening with commas all those variables
     * following their order of appearance in the corresponding template.
     * For example, the group id of a table with two variables named product and
     * price will be md5('product,price')
     * 
     * @param array data an array of arrays with the folowing key values:
     *      'id': the id of the required template
     *      'settings': an array of arrays with the following key value pairs:
     *         'numberFormat': can bw ".;" or ",."
     *         'outputComments' (boolean)
     *         'outputFormat': an array with the possible, non-exclusive, values
     *          ["odt", "pdf", "doc", "docx", "doc-legacy", "rtf"]
     *     'variables': an array of arrays with the following key value pairs:
     *         'variable name': an array with the following key value pairs:
     *             'scope': can be document, form or both (default value)
     *             'label' (text)
     *             'tip' (text)
     *             'comment' (HTML text)
     *             'type': it can be text, options, date or phone.
     *             'richtext' (boolean) only applies if the type is text.
     *             'choice': dropdown, checkbox or radio. Only applies if the
     *               type is options.
     *             'options': ";" separated list of values. Only applies if the
     *              type takes the "options" value
     *             'compulsory'(boolean)
     *             'editable' (boolean)
     *             'global' (boolean)
     *             'confirm' (boolean)
     *             'validation' (string) validation name (only relevant to
     *              identify the validation in the web edition interface)
     *             'regex': regular expression used to validate this field
     *     'groups': an array of arrays with the following key value pairs:
     *          'group id': an array with the following key value pairs:
     *             'active' (boolean) if true (default value) this group
     *              is clonable
     *             'display': can be show (default) or hide
     *             'print': can be print (default), unprint (only visible in
     *              the browser) or unbrowsable (only printed and not visible
     *              in the browser)
     *             'toggleWith' (text)
     *             'toggleValues' (text)
     *  
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def modifyTemplateData(self, data, callback = ''):
        
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/modify_template/' + str(data['id'])

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
        
        options = {}
        options['id'] = data['id']
        if (self.isset(data,'settings')):
            options['settings'] = data['settings']
        else :
            options['settings'] = {}
        
        if (self.isset(data,'variables')):
            options['variables'] = data['variables']
        else :
            options['variables'] = {}
        
        if (self.isset(data,'groups')):
            options['groups'] = data['groups']
        else :
            options['groups'] = {}
        
		
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
       
        return self._returnLink(url, data['id'], opt)
    


    """
     * Allows to remotely authenticate from any other application into the
     * associated Docxpresso SERVER installation
     * 
     * @param array $data $data with the following keys and values
     *      'email' => (string) the email of the user we want to log in.
     *       This value is compulsory and must correspond to a valid registered
     *       user email.
     *      'url' => (string) target url where the user should be redirected
     *       after being authenticated
     *      'referer' => (string) domain origin of the petition
     * @return string
     * @access public
    """
    def accessByTokenAction(self, data):
    
        url = str(self._options['docxpressoInstallation']) + '/users/accessByToken'

        options = {}
        options['email'] = data['email']
        options['url'] = data['url']
        if not(self.empty(data,'referer')):
            options['referer'] = data['referer']
        
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
      
        return self._returnLink(url, None, opt);    
    

    """
     * Allows to remotely create an user
     * 
     * @param array $data $data with the following keys and values
     *      'username' => (string) alias to be used within Docxpresso.
     *       This value is compulsory and can not coincide with the username 
     *       of an already registered user.
     *      'email' => (string) the email of the user we want to create.
     *       This value is compulsory and can not coincide with the email of an
     *       existing user.
     *      'password' => (string) the password of the user we want to create.
     *       This value is compulsory and must be safe.
     *      'name' => (string) full user name (compulsory)
     *      'role' => (string) it must take one of the following values: admin,
     *       editor, user, external. Default value is user.
     *      'position' => (string) user position (optional)
     *      'phone' => (string) user phone (optional)
     *      'description' => (string) short user description (optional)
     * @return string
     * @access public
    """
    def createUser(self, data):
     
        url = str(self._options['docxpressoInstallation']) + '/users/createRemoteUser'

        options = {}
        options['email'] = data['email']
        options['username'] = data['username']
        options['password'] = data['password']
        options['name'] = data['name']
        if (data['role'] == "admin"):
            options['role'] = 3
        elif (data['role'] == "editor"):
            options['role'] = 2
        elif (data['role'] == "user"):
            options['role'] = 1
        elif (data['role'] == "external"):
            options['role'] = 0
        
        if (self.isset(data,'position')):
            options['position'] = data['position']
        else:
            options['position'] = " "
        
        if (self.isset(data,'phone')):
            options['phone'] = data['phone']
        else :
            options['phone'] = " "
        
        if (self.isset(data,'description')):
            options['description'] = data['description']
        else:
            options['description'] = " "
        

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
      
        return self._returnLink(url, None, opt);     
    

    """     
     * Create a workflow
     * 
     * @param array $data with the following keys and values
     *      'template' => (int) the id of the requested document template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'description' => (string) short (HTML) description of the workflow
     *       to be used in automated emails.
     *      'token' => (string) a unique identifier of a previous use. If given
     *       the data associated with the token will be preloaded into 
     *       the document. The default value is NULL.
     *      'ordered' => (boolean) if true (default value) the workflow will be
     *       an ordered workflow.
     *      'display' => (string) it can be 'document' (default) or 'form'.
     *      'steps' => (array) the steps should be an array of arrays each of 
     *       them with the following keys and values:
     *          'username' => (string) the name of the user associated with that
     *           step.
     *          'useremail' => (string) the email of the user associated with
     *           that step.
     *          'action' => (string) the associated action. It can take the
     *           following values: 'edit' (default value) or 'validate'.
     *          'rejectionAction' => (string) the action to be taken if a 
     *           validation is rejected. It can take the following values:
     *           'stepBack' (default value) or 'complete'.
     *          'notify' => (boolean) if true (default value) the user will be
     *           notified by email.
     *          'send' => (boolean) if true (default value) the user will
     *           receive a copy of the document upon completion of the workflow.
     *          'prefix' => (string) a prefix that will limit enduser edition to
     *           only the field variables that start by that prefix. You can use
     *           a comma separated list to select more than one prefix. Default 
     *           value is an empty string.
     *          'editableVars' => (string) a comma separated list of var names
     *           to restrict the edition to that set. Default value is an empty 
     *           string.
     *     
     * @return string
     * @access public
     """
    def createWorkflow(self, data, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/documents/workflow/create_remote_workflow/' + str(data['template'])
        workflow = {}

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
        options = {}
        if (self.isset(data,'token')) :
            options['token'] = data['token']
        
        if (self.isset(data,'display')):
            options['display'] = data['display']
        
        if ((self.isset(data,'ordered')) and (not(data['ordered']))) :
            workflow['ordered'] = 0
        else :
            workflow['ordered'] = 1
        
        if (self.isset(data,'description')) :
            workflow['description'] = data['description']
        else:
            workflow['description'] = ''
        
        #workflow steps
        workflow['steps'] = {}
        numSteps = len(data['steps'])
        j=0
        while j < numSteps:
            workflow['steps'][j] = {}
            workflow['steps'][j]['completed'] = 0
            if (self.isset(data['steps'][j],'notify') and not(data['steps'][j]['notify'])) :
                workflow['steps'][j]['notify'] = 0
            else :
                workflow['steps'][j]['notify'] = 1
            
            if (self.isset(data['steps'][j],'send') and not(data['steps'][j]['send'])) :
                workflow['steps'][j]['send'] = 0
            else :
                workflow['steps'][j]['send'] = 1
            
            if (self.isset(data['steps'][j],'action') and data['steps'][j]['action'] == 'validate') :
                workflow['steps'][j]['actionType'] = 'validate'
            else:
                workflow['steps'][j]['actionType'] = 'edit'
            
            if (self.isset(data['steps'][j],'rejectionAction') and data['steps'][j]['rejectionAction'] == 'complete') :
                workflow['steps'][j]['rejectionAction'] = 'completedWF'
            else :
                workflow['steps'][j]['rejectionAction'] = 'stepBack'
            
            if (self.isset(data['steps'][j],'prefix')) :
                workflow['steps'][j]['prefix'] = data['steps'][j]['prefix']
            else:
                workflow['steps'][j]['prefix'] = ''
            
            if (self.isset(data['steps'][j],'editableVars')) :
                workflow['steps'][j]['editableVars'] = data['steps'][j]['editableVars']
            else:
                workflow['steps'][j]['editableVars'] = ''
            
            workflow['steps'][j]['useremail'] = data['steps'][j]['useremail']
            workflow['steps'][j]['username'] = data['steps'][j]['username']
            j += 1
        
        options['workflow'] = workflow
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
        
        return self._returnLink(url, data['template'], opt);  
    

    """
     * Returns a link to recover the info about a certain workflow by id
     * 
     * @param integer $id the workflow id
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def getWorkflowData(self, id, callback = ''):
        
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/workflowData/' + str(id)
        
        if (callback != '' and callback != None) :
            url += '/' + str(callback)
       
        return self._returnLink(url, id)
    

    """
     * Returns a link to list of categories in JSON(P) format from the associated
     * Docxpresso SERVER installation
     * 
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def listCategories(self, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/categories'
        
        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
       
        return self._returnLink(url)
    

    """
     * Returns a link to list of documents in a given category in JSON(P) format
     * from the associated Docxpresso SERVER installation
     * 
     * @param integer $category the corresponding category id.
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @param boolean $published if true only "published" templates will be
     * available through the request.
     * @param string $access it can be "all" (deafult value), "public" for only
     * documents declared like public or a "username" to filter by permissions
     * @return string
     * @access public
    """
    def documentsByCategory(self, category, callback = '', published = 0, access = 'all'):
     
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/documents_by_category/' + str(category)

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        else :
            url += '/NULL'
        

        if (published != '' and published != None) :
            url += '/1'
        else:
            url += '/0'
        
        
        if (access != '' and access != None) :
            url += '/' + quote(access)
        
		
        return self._returnLink(url)
    

    """
     * Allows to change the password associated with a user email.
     * 
     * @param string $email user unique email identifier.
     * @param string $password new password. It should be, at least 12 chars long
     * and contain at least an uppercase letter, a lowercase letter, a number
     * and a non-standard char: !,%,&,@,#,$,^,*,?,_,~
     * @param boolean $notify set it to true (default value) if you want to
     * the user of the password change
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def modifyPassword(self, email, password, notify = True, callback = ''):
      
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/modify_password'

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
        options = {}
        options['email'] = email
        options['password'] = password
        options['notify'] = notify

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
        return self._returnLink(url, None, opt)
    

    """
     * Allows to modify the configuration of Signature Providers. If the
     * requested signature provider does not exist and it belongs to one of
     * the current available ones the corresponding entry will be created.
     * 
     * @param string $provider the name of the signature provider. Currently
     * the only available ones are vidSigner, lleida.net or nodalblock
     * @param string $config base64 encoded config JSON.
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def modifySignatureProvider(self, provider, config, callback = ''):
        
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/modify_signature_providers/' + str(provider)

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
        options = {}
        options['custom'] = config

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
        return self._returnLink(url, None, opt)
    

    """
     * Returns a link to download the whole document (sub)tree in JSON(P) format  
     * from the associated Docxpresso SERVER installation
     * 
     * @param mixed $rootCategory the corresponding category id from which
     * we want to build the document tree. Default value is 'root' that corresponds
     * with the "root category"
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @param boolean $published if true only "published" templates will be
     * available through the request.
     * @param string $access it can be "all" (deafult value), "public" for only
     * documents declared like public or a "username" to filter by permissions
     * @return string
     * @access public
    """
    def documentTree(self, rootCategory= 'root', callback = '', published = 0, access = 'all'):
        
        if (rootCategory == 'root') :
            rootCategory = 1
        
        
        url = str(self._options['docxpressoInstallation'])  + '/RESTservices/predefined/document_tree/' + str(rootCategory)

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        else :
            url += '/NULL'
        

        if (published != '' and published != None) :
            url += '/1'
        else :
            url += '/0'
        
        
        if (access != '' and access != None) :
            url += '/' + quote(access)
        

        return self._returnLink(url)
    

    """
     * Returns a link to download the whole category (sub)tree in JSON(P) format  
     * from the associated Docxpresso SERVER installation. If you need to include
     * documents use the documentTree method instead.
     * 
     * @param mixed $rootCategory the corresponding category id from which
     * we want to build the document tree. Default value is 'root' that corresponds
     * with the "root category"
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def categoryTree(self, rootCategory= 'root', callback = ''):
       
        if (rootCategory == 'root') :
            rootCategory = 1
        
        
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/category_tree/' + str(rootCategory)

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        else :
            url += '/NULL'
        

        return self._returnLink(url)
    

    """
     * Returns a link to download all documents with a given name in JSON(P)  
     * format from the associated Docxpresso SERVER installation
     * 
     * @param string $name the name of the template we are looking for. This
     * method launches a "LIKE" SQL query.
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @param boolean $published if true only "published" templates will be
     * available through the request.
     * @param string $access it can be "all" (deafult value), "public" for only
     * documents declared like public or a "username" to filter by permissions
     * @return string
     * @access public
    """
    def templatesByName(self, name, callback = '', published = 0, access = "all"):
    
        url = str(self._options['docxpressoInstallation'])
        url += '/RESTservices/predefined/documents_by_name/' + str(quote(name))

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        else :
            url += '/NULL'
        

        if (published != '' and published != None) :
            url += '/1'
        else:
            url += '/0'
        
        
        if (access != '' and access != None) :
            url += '/' + quote(access)
        

        return self._returnLink(url)
     

    """
     * Returns a link to download the info (thumbnail included) of the most
     * recently edited templates
     * 
     * @param string $limit the number of templates we want to retrieve.
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @param boolean $published if true only "published" templates will be
     * available through the request.
     * @return string
     * @access public
    """
    def latestTemplates(self, limit, callback = '', published = 0):
    
        url = str(self._options['docxpressoInstallation'])
        url += '/RESTservices/predefined/latest_templates/' + str(limit)

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        else :
            url += '/NULL'
        

        if (published != '' and published != None) :
            url += '/1'
        else:
            url += '/0'
        

        return self._returnLink(url)
    


    """
     * Returns a link to get all templates ids that have certain Tags
     * 
     * @param array $data with the following keys and values
     *      'tags' => (array) list of tags to be searche for
     *      'category' => (integer) the category we want to filter by if any.
     *       Subcategories are not included.
     *      'published' => (boolean) if true only published templates are
     *       returned.
     *      'active' => (boolean)if true (default value) only "non-deleted"
     *       tempaltes are returned.
     *      'sort' => (string) the field used to sort the results.
     *      'order' => (string) possible values are DESC (default) or ASC.
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * available through the request.
     * @return string
     * @access public
     """
    def searchTemplatesByTag(self, data, callback = ''):
        
        url = str(self._options['docxpressoInstallation'])
        url += '/RESTservices/predefined/search_templates_by_tags'

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        else :
            url += '/NULL'
        

        #we build and options object with the search filters
        options = {}
        if not(self.empty(data,'tags')) :
            options['tags'] = data['tags']
        
        if not(self.empty(data,'category')) :
            options['category'] = data['category']
        
        if (self.isset(data,'published')) :
            options['published'] = data['published']
        
        if (self.isset(data,'active')) :
            options['active'] = data['active']
        
        if not(self.empty(data,'sort')) :
            options['sort'] = data['sort']
        
        if not(self.empty(data,'order')) :
            options['order'] = data['order']
        
        

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))

        return self._returnLink(url, None, opt);
    

    """
     * Returns a link to list all documents with a given name and/or a   
     * given category from the associated Docxpresso SERVER installation
     * 
     * @param integer $page the page we want to retrieve
     * @param array $data with the following keys and values
     *      'name' => (string) the name we want to filter the results with a 
     *       LIKE%% clause. This parameter is optional.
     *      'category' => (integer) the category we want to filter by if any.
     *       Subcategories are not included.
     *      'numResults' => (int) number of results per page. This number can 
     *       not be bigger than 100 and it defaults to 20.
     *      'sort' => (string) the field used to sort the results.
     *      'order' => (string) possible values are DESC (default) or ASC.
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def listTemplatesPaginated(self, page, data = {}, callback = ''):
        
        url = str(self._options['docxpressoInstallation'])
        url += '/RESTservices/predefined/list_templates_paginated/' + str(page)

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
        
        #we build and options object with the search filters
        options = {}
        if not(self.empty(data,'name')) :
            options ['identifier'] = data['name']
        
        if not(self.empty(data,'numResults')) :
            options['numResults'] = data['numResults']
        
        if not(self.empty(data,'category')) :
            options['category'] = data['category']
        
        if not(self.empty(data,'sort')) :
            options['sort'] = data['sort']
        
        if not(self.empty(data,'order')) :
            options['order'] = data['order']
        
        

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))

        return self._returnLink(url, None  , opt)



    """
     * Returns a link to download the data of a given single usage JSON(P)  
     * format from the associated Docxpresso SERVER installation
     * 
     * @param integer $limit the max numbers of uses to be downloaded. This
     * parameter is compulsory. If bigger then the max allowed limit the number
     * of results will be truncated.
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def lastUsages(self, limit, callback = ''):
        
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/last_usages/' + str(limit)

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
		
        return self._returnLink(url)
    

    """
     * Returns a list of the lestest used templates
     * 
     * @param integer $limit the max numbers of uses to be downloaded. This
     * parameter is compulsory. If bigger then the max allowed limit the number
     * of results will be truncated. Default number is 10.
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def lastUsedTemplates(self, limit = 10, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/last_used_templates/' + str(limit)

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
		
        return self._returnLink(url)
    

    """
     * Returns a link to download all template usage data in JSON(P)  
     * format  for a given template id from the associated Docxpresso 
     * SERVER installation
     * 
     * @param array $data with the following keys and values
     *      'id' => (int) the id of the template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'identifier' => (string) the identifier field of an usage. The
     *       default value is an empty string
     *      'reference' => (string) the reference field of an usage. The
     *       default value is an empty string
     *      'enduserid' => (string) the end user id of a particular usage.
     *       Default value is an empty string.
     *      'period' => (string) if given will overwrite the given startDate and
     *       enddate parameters. The possible values are: today, 
     *       1week (last week), 1month (last month), 3month (last quarter),
     *       year (last year). The default value is empty
     *      'startDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened after it. Default value is an empty 
     *       string. Optionally you may include de time in the format hh:mm:ss
     *      'endDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened before it. Default value is an empty 
     *       string. Optionally you may include de time in the format hh:mm:ss
     *      'locked' => (integer) it can be zero for all usages (default), 1 if
     *       we only want usages that have been set as completed or 2 for the 
     *       opposite.
     *      'firstResult' => (int) query offset. Default value is 0; 
     *      'maxResults' => (int) maximum number of results. Beware that
     *       each installation may have upper limits to this number.
     *       Default value is empty and Docxpresso default will be used (50).
     *      'sort' => (string) the field used to sort the results.
     *      'order' => (string) possible values are DESC (default) or ASC.
     *      'client' => (integer) cliend id. Only for multi tenant instances. 
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def dataByTemplate(self, data, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/data_by_template/' + str(data['id'])
		
        if (callback != '' and callback != None) :
                url += '/' + str(callback)
        

        #we build and options object with the search filters
        options = {}
        if not(self.empty(data,'identifier')) :
            options['identifier'] = data['identifier']
        
        if not(self.empty(data,'client')) :
            options['client'] = data['client']
        
        if not(self.empty(data,'reference')) :
            options['reference'] = data['reference']
        
        if not(self.empty(data,'enduserid')) :
            options['enduserid'] = data['enduserid']
        
        if not(self.empty(data,'locked')) :
            options['locked'] = data['locked']
        
        #dates must be in the format 2016-01-30
        if not(self.empty(data,'startDate')) :
            options['startDate'] = data['startDate']
        
        if not(self.empty(data,'endDate')) :
            options['endDate'] = data['endDate']
        
        if not(self.empty(data,'period')) :
            options['period'] = data['period']
        
        if not(self.empty(data,'firstResult')) :
            options['firstResult'] = data['firstResult']
        
        if not(self.empty(data,'maxResults')) :
            options['maxResults'] = data['maxResults']
        
        if not(self.empty(data,'sort')) :
            options['sort'] = data['sort']
        
        if not(self.empty(data,'order')) :
            options['order'] = data['order']
        

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
		
        return self._returnLink(url, data['id'], opt)
    


    """
     * Returns a link to download the 'paginated' template usage data in JSON(P)  
     * format  for a given template id from the associated Docxpresso 
     * SERVER installation
     * 
     * @param integer $page the page we want to retrieve
     * @param array $data with the following keys and values
     *      'id' => (int) the id of the template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'identifier' => (string) the identifier field of an usage. The
     *       default value is an empty string
     *      'reference' => (string) the reference field of an usage. The
     *       default value is an empty string
     *      'enduserid' => (string) the end user id of a particular usage.
     *       Default value is an empty string.
     *      'period' => (string) if given will overwrite the given startDate and
     *       enddate parameters. The possible values are: today, 
     *       1week (last week), 1month (last month), 3month (last quarter),
     *       year (last year). The default value is empty
     *      'startDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened after it. Default value is an empty 
     *       string.
     *      'endDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened before it. Default value is an empty 
     *       string.
     *      'locked' => (integer) it can be zero for all usages (default), 1 if
     *       we only want usages that have been set as completed or 2 for the 
     *       opposite.
     *      'numResults' => (int) number of results per page. This number can 
     *       not be bigger than 100 and it defaults to 20.
     *      'sort' => (string) the field used to sort the results.
     *      'order' => (string) possible values are DESC (default) or ASC.
     *      'client' => (integer) cliend id. Only for multi tenant instances. 
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def dataByTemplatePaginated(self, page, data, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/data_by_template_paginated/' + str(data['id']) + '/' + str(page)
		
        if (callback != '' and callback != None) :
                url += '/' + str(callback)
        

        #we build and options object with the search filters
        options = {}
        if not(self.empty(data,'identifier')) :
            options['identifier'] = data['identifier']
        
        if not(self.empty(data,'client')) :
            options['client'] = data['client']
        
        if not(self.empty(data,'reference')) :
            options['reference'] = data['reference']
        
        if not(self.empty(data,'enduserid')): 
            options['enduserid'] = data['enduserid']
        
        if not(self.empty(data,'locked')) :
            options['locked'] = data['locked']
        
        #dates must be in the format 2016-01-30
        if not(self.empty(data,'startDate')) :
            options['startDate'] = data['startDate']
        
        if not(self.empty(data,'endDate')) :
            options['endDate'] = data['endDate']
        
        if not(self.empty(data,'period')):
            options['period'] = data['period']
        
        if not(self.empty(data,'numResults')) :
            options['numResults'] = data['numResults']
        
        if not(self.empty(data,'sort')) :
            options['sort'] = data['sort']
        
        if not(self.empty(data,'order')) :
            options['order'] = data['order']
        

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
		
        return self._returnLink(url, data['id'], opt)
    

    """
     * Returns a link to download the 'paginated' template usage data in JSON(P)  
     * format from the associated Docxpresso SERVER installation
     * 
     * @param integer $page the page we want to retrieve
     * @param array $data with the following keys and values
     *      'id' => (int) the id of the template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'identifier' => (string) the identifier field of an usage. The
     *       default value is an empty string
     *      'reference' => (string) the reference field of an usage. The
     *       default value is an empty string
     *       'domain' => (string) the domain field of an usage. The
     *       default value is an empty string
     *      'enduserid' => (string) the end user id of a particular usage.
     *       Default value is an empty string.
     *      'period' => (string) if given will overwrite the given startDate and
     *       enddate parameters. The possible values are: today, 
     *       1week (last week), 1month (last month), 3month (last quarter),
     *       year (last year). The default value is empty
     *      'startDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened after it. Default value is an empty 
     *       string.
     *      'endDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened before it. Default value is an empty 
     *       string.
     *      'locked' => (integer) it can be zero for all usages (default), 1 if
     *       we only want usages that have been set as completed or 2 for the 
     *       opposite.
     *      'numResults' => (int) number of results per page. This number can 
     *       not be bigger than 100 and it defaults to 20.
     *      'sort' => (string) the field used to sort the results.
     *      'order' => (string) possible values are DESC (default) or ASC.
     *      'client' => (integer) cliend id. Only for multi tenant instances. 
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def getUsageDataPaginated(self, page, data, callback = ''):
     
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/get_usage_data_paginated/' + str(page)
		
        if (callback != '' and callback != None) :
                url += '/' + str(callback)
        

        #we build and options object with the search filters
        options = {}
        if not(self.empty(data,'id')) :
            options['id'] = data['id']
        
        if not(self.empty(data,'identifier')) :
            options['identifier'] = data['identifier']
        
        if not(self.empty(data,'client')) :
            options['client'] = data['client']
        
        if not(self.empty(data,'reference')) :
            options['reference'] = data['reference']
        
        if not(self.empty(data,'enduserid')) :
            options['enduserid'] = data['enduserid']
        
        if not(self.empty(data,'domain')) :
            options['domain'] = data['domain']
        
        if not(self.empty(data,'locked')) :
            options['locked'] = data['locked']
        
        #dates must be in the format 2016-01-30
        if not(self.empty(data,'startDate')) :
            options['startDate'] = data['startDate']
        
        if not(self.empty(data,'endDate')) :
            options['endDate'] = data['endDate']
        
        if not(self.empty(data,'period')):
            options['period'] = data['period']
        
        if not(self.empty(data,'numResults')) :
            options['numResults'] = data['numResults']
        
        if not(self.empty(data,'sort')) :
            options['sort'] = data['sort']
        
        if not(self.empty(data,'order')) :
            options['order'] = data['order']
        

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
		
        return self._returnLink(url, None, opt)
    

    """
     * Returns a link to download the data of a given single usage JSON(P)  
     * format from the associated Docxpresso SERVER installation
     * 
     * @param integer $usageId the id of a particular usage
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def dataByUsage(self, usageId, callback = ''):
      
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/data_by_usage/' + str(usageId)

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
		
        return self._returnLink(url, usageId)
    

    """
     * Returns a link to generate a HTML or CSV file for all the data usage
     * for a given template  
     * 
     * @param array $data with the following keys and values
     *      'id' => (int) the id of the template. This value is compulsory and 
     *       must correspond to a valid template id.
     *      'format' => (string) it may be html or csv (default)
     *      'identifier' => (string) the identifier field of an usage. The
     *       default value is an empty string
     *      'reference' => (string) the reference field of an usage. The
     *       default value is an empty string
     *      'enduserid' => (string) the end user id of a particular usage.
     *       Default value is an empty string.
     *      'idrange' => (string) the range of ids that should be filtered, i.e.
     *       120-145. Default value is an empty string.
     *      'period' => (string) if given will overwrite the given startDate and
     *       enddate parameters. The possible values are: today, 
     *       1week (last week), 1month (last month), 3month (last quarter),
     *       year (last year). The default value is empty
     *      'startDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened after it. Default value is an empty 
     *       string.
     *      'endDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened before it. Default value is an empty 
     *       string.
     *      'locked' => (integer) it can be zero for all usages (default), 1 if
     *       we only want usages that have been set as completed or 2 for the 
     *       opposite.
     *      'firstResult' => (int) query offset. Default value is 0; 
     *      'maxResults' => (int) maximum number of results. Beware that
     *       each installation may have upper limits to this number.
     *       Default value is an empty and in that case Docxpresso
     *      'sort' => (string) the field used to sort the results.
     *      'order' => (string) possible values are DESC (default) or ASC.
     *      'client' => (integer) cliend id. Only for multi tenant instances. 
     * @return string
     * @access public
    """
    def dataDigestByUsage(self, data):
    
        url = str(self._options['docxpressoInstallation']) + '/data/digest/' + str(data['id'])

        url = str(self._returnLink(url, data['id'], None)) + '&'

        #  we build the URL with the search filters and output format
        if not(self.empty(data,'format')) :
            url += 'format=' + data['format'] + '&'
        else :
            url += 'format=csv&'
        
        if not(self.empty(data,'identifier')) :
            url += 'identifier=' + data['identifier'] + '&'
        
        if not(self.empty(data,'client')) :
            url += 'client=' + data['client'] + '&'
        
        if not(self.empty(data,'reference')) :
            url += 'reference=' + data['reference'] + '&'
        
        if not(self.empty(data,'enduserid')) :
            url += 'enduserid=' + data['enduserid'] + '&'
        
        #dates like before and after must be in the format 2016-01-30
        if not(self.empty(data,'startDate')) :
            url += 'before=' + data['startDate'] + '&'
        
        if not(self.empty(data,'endDate')) :
            url += 'after=' + data['endDate'] + '&'
        
        if not(self.empty(data,'period')) :
            url += 'period=' + data['period'] + '&'
        
        if not(self.empty(data,'domain')) :
            url += 'domain=' + data['domain'] + '&'
        
        if not(self.empty(data,'idrange')) :
            url += 'idrange=' + data['idrange'] + '&'
        
        if not(self.empty(data,'locked')) :
            url += 'locked=' + data['locked'] + '&'
        
        if not(self.empty(data,'maxResults')) :
            url += 'maxResults=' + data['maxResults'] + '&'
        
        if not(self.empty(data,'sort')) :
            url += 'sort=' + data['sort'] + '&'
        
        if not(self.empty(data,'order')) :
            url += 'order=' + data['order']
        
        url += 'extra=1'
        return self._returnLink(url, data['id'])


    """
     * Returns a link to download all template forwarded docs in JSON(P)  
     * format  for a given template id from the associated Docxpresso 
     * SERVER installation
     * 
     * @param array $data with the following keys and values
     *      'id' => (int) the id of the template.
     *       This value is compulsory and must correspond to a valid template
     *       id.
     *      'identifier' => (string) the identifier field of an usage. The
     *       default value is an empty string
     *      'reference' => (string) the reference field of an usage. The
     *       default value is an empty string
     *      'processed' => (integer) a flag that allows to set the processing
     *       status. By default forwarded documents have a processed status of
     *       0. This processed status may be managed remotely via the
     *       fetchForwardedDocument method of the SDK
     *      'period' => (string) if given will overwrite the given startDate and
     *       enddate parameters. The possible values are: today, 
     *       1week (last week), 1month (last month), 3month (last quarter),
     *       year (last year). The default value is empty
     *      'startDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened after it. Default value is an empty 
     *       string.
     *      'endDate' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened before it. Default value is an empty 
     *       string.
     *      'firstResult' => (int) query offset. Default value is 0; 
     *      'maxResults' => (int) maximum number of results. Beware that
     *       each installation may have upper limits to this number.
     *       Default value is empty and Docxpresso default will be used (50).
     *      'sort' => (string) the field used to sort the results.
     *      'order' => (string) possible values are DESC (default) or ASC.
     *      'client' => (integer) cliend id. Only for multi tenant instances. 
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def forwardedDocumentsByTemplate(self, data, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/forwarded_documents_by_template/' + str(data['id'])
		
        if (callback != '' and callback != None) :
                url += '/' + str(callback)
        

        #we build and options object with the search filters
        options = {}
        if not(self.empty(data,'identifier')) :
            options ['identifier'] = data['identifier']
        
        if not(self.empty(data,'client')) :
            options['client'] = data['client']
        
        if not(self.empty(data,'reference')) :
            options['reference'] = data['reference']
        
        if not(self.empty(data,'processed')) :
            options['processed'] = data['processed']
        
        #dates must be in the format 2016-01-30
        if not(self.empty(data,'startDate')) :
            options['startDate'] = data['startDate']
        
        if not(self.empty(data,'endDate')) :
            options['endDate'] = data['endDate']
        
        if not(self.empty(data,'period')) :
            options['period'] = data['period']
        
        if not(self.empty(data,'firstResult')) :
            options['firstResult'] = data['firstResult']
        
        if not(self.empty(data,'maxResults')) :
            options['maxResults'] = data['maxResults']
        
        if not(self.empty(data,'sort')) :
            options['sort'] = data['sort']
        
        if not(self.empty(data,'order')) :
            options['order'] = data['order']
        

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
		
        return self._returnLink(url, data['id'], opt)
    

    """
     * Returns a link to modify the data and options of a particular usage.
     * In order to avoid unwanted/accidental changes of data we request together
     * with the usageId its unique assocated token
     * 
     * 
     * @param integer $usageId the id of a particular usage
     * @param array $data with the following keys and values
     *      'token' => (string) the unique identifier of this use. This is
     *       only required for security to avoid unintentional changes in the 
     *       usage data.
     *      'identifier' => (string) the identifier value that we want to
     *       overwrite. Default value is an empty string 
     *      'reference' => (string) the reference value that we want to
     *       overwrite. Default value is an empty string 
     *      'validated' => (boolean) an optional boolean parameter to overwrite
     *       the previous value.
     *      'tampered' => (boolean) an optional boolean parameter to overwrite
     *       the previous value.
     *      'locked' => (boolean) an optional boolean parameter to overwrite
     *       the previous value. It is also may be interpreted as "completed"
     *      'domain' => (string) an optional parameter to overwrite the domain
     *       property.
     *      'user' => (string) an optional parameter to overwrite the user
     *       name associated with the selected usage.
     *       the previous value. It is also may be interpreted as "completed"
     *      'comments' => (string) if not empty it will overwrite the comments
     *       associated with this usage. Default value is an empty 
     *       string.
     *      'percentageCompleted' => (integer) if given  overwrites the value of
     *       the percentage completed. 
     *       string.
     *      'varData' => JSON data that will be merged with the previous stored
     *       document data (by the time being only variable values).
     *      'callback' => function name for JSONP calls.
     *      'plugin' => (boolean) if true the petition may directly come from
     *       a plugin user so further security checks may be carried out to test
     *       for data coherence and permissions.
     * @return string
     * @access public
    """
    def modifyUsageData(self, usageId, data):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/modify_usage_data/' + str(usageId)
        
        options = {}
        if (self.isset(data,'token')) :
            options['token'] = data['token']
        
        if (self.isset(data,'identifier')) :
            options['identifier'] = data['identifier']
        
        if (self.isset(data,'reference')): 
            options['reference'] = data['reference']
        
        if (self.isset(data,'domain')) :
            options['domain'] = data['domain']
        
        if (self.isset(data,'user')) :
            options['enduserid'] = data['user']
        
        if (self.isset(data,'tampered') and data['tampered']) :
            options['tampered'] = 1
        elif (self.isset(data,'tampered') and not(data['tampered'])) :
            options['tampered'] = 0
        
        if (self.isset(data,'validated') and data['validated']) :
            options['validated'] = 1
        elif (self.isset(data,'validated') and not(data['validated'])) :
            options['validated'] = 0
        
        if ((not(self.empty(data,'locked'))) and data['locked']) :
            options['locked'] = 1
        elif (self.isset(data,'locked') and not(data['locked'])) :
            options['validated'] = 0
        
        if not(self.empty(data,'comments')) :
            options['comments'] = data['comments']
        
        if (self.isset(data,'varData')) :
            options['data'] = data['varData']
        
        if (self.isset(data,'callback')) :
            options['callback'] = data['callback']
        
        if (self.isset(data,'plugin')) :
            options['plugin'] = data['plugin']

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
        return self._returnLink(url, usageId, opt)
    


    """
     * Returns a link to get a JSON with both the document base64 encoded 
     * together with the other usage data 
     * 
     * @param integer $usageId the id of a particular usage
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def documentAndDataByUsage(self, usageId, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/document_and_data_by_usage/' + str(usageId)

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
		
        return self._returnLink(url, usageId)
    

    """
     * Returns a link to download basic statistical data like number of uses
     * and last usage
     * 
     * @param mixed $id template id. If set to 'all' the data
     * for all available templates will be provided
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty or NULL plain JSON will be returned.
     * @param boolean $published if true only "published" templates will be
     * available through the request.
     * @return string
     * @access public
    """
    def dataStatistics(self, id = 'all', callback = '', published = 0):
    
        url = self._options['docxpressoInstallation'] + '/RESTservices/predefined/data_statistics';
		
        if (id != '' and id != None) :
            url += '/' + id
        else :
            url += '/all'
        
		
        if (callback != '' and callback != None):
            url += '/' + callback
        elif (published != '' and published != None) :
            url += '/NULL'
        

        if (published != '' and published != None) :
            url += '/1'
        

        return self._returnLink(url, id)
    


    """
     * Returns a link to download the total usage count group by day 
     * 
     * @param array $data with the following keys and values
     *      'id' => (mixed) the id of the template. If set to 'all' the data
     *       for all available templates will be provided.
     *      'after' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened after it. Default value is an empty 
     *       string.
     *      'before' => (string) a date in the format yyyy-mm-dd that will
     *       select usages that happened before it. Default value is an empty 
     *       string.
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty or NULL plain JSON will be returned.
     * @return string
     * @access public
    """
    def usageCount(self, data = {}, callback = ''):
    
        if not(self.isset(data,'id')) :
            data['id'] = 'all'
        
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/usage_count/' + str(data['id'])
		
        if (callback != '' and callback != None) :
            url += '/' + callback
        

        #we build and options object with the search filters
        options = {}
        if not(self.empty(data,'before')) :
            options['before'] = data['before']
        
        if not(self.empty(data,'after')) :
            options['after'] = data['after']
        

        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
		
        return self._returnLink(url, data['id'], opt)
    

    """
     * Returns a link to list of users in JSON(P) format from the associated
     * Docxpresso SERVER installation
     * 
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def userList(self, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/users'

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
       
        return self._returnLink(url)
    

    """
     * Returns a link to check if the the user is logged into the associated
     * Docxpresso SERVER installation
     * 
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """
    def checkUser(self, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/check_user'

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        
       
        return self._returnLink(url)
    


    """
     * Returns a link to clone a template
     * 
     @param integer $id the id of the template we want to clone
     * @param array $data with the following keys and values
     *      'name' => (string) the name given to the cloned template.
     * @return string
     * @access public
    """
    def cloneTemplate(self, id, data = {}, callback = ''):
    
        url = str(self._options['docxpressoInstallation']) + '/RESTservices/predefined/clone_template/' + str(id)

        if (callback != '' and callback != None) :
            url += '/' + id(callback)
        
        
        #we build and options object
        options = {}
        if not(self.empty(data,'name')) :
            options['name'] = data['name']
        

       
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
        return self._returnLink(url, id, opt)
    

    """
     * Returns a link to use in a form or via a cURL POST
     * The post fields should include:
     *  'email' the valid email of a registered Docxpresso EDITOR/ADMIN user
     *  'path' a file input field
     *  'name' a unique name for the new template
     *  'config' an array JSON encoded with additional configuration options
     *  'category' the category id where the template should be stored
     *  'tags' a comma separated string of tags associated with the template (optional)
     *  'public' a boolean value (1 or 0) setting internal write/read permissions for
     *   editors. Default value is 1 (all editors have access).
     *  'accessControl' a boolean value (1 or 0). If equals 0 there is free
     *   access to that document by end users. Default value is 1.
     *  'description' an optional description
     * 
     @param integer $id the id of the template we want to update
     * @param array $data with the following keys and values
     *      'responseURL' => redirect URL if used as an action in a form.
     *      'callback' => (string) the callback function if called as JSONP.
     * @return string
     * @access public
    """
    def createTemplate(self, data = {}):
    
        id = int(math.floor(random.randint(99999,99999999)))
        print(id)
        url = str(self._options['docxpressoInstallation']) + '/documents/remote_create_template/' + str(id)
        
        #we build and options object
        options = {}
        if not(self.empty(data,'responseURL')) :
            options['responseURL'] = data['responseURL']
        
        if not(self.empty(data,'callback')) :
            options['callback'] = data['callback']
        
       
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
        return self._returnLink(url, id, opt)
    


    """
     * Returns a link to use in a form or via a cURL POST
     * The post fields should include:
     *  'path' a file input field
     *  'keepThumb' a field that if not empty will preserve the current
     *   document thumbnail
     * 
     @param integer $id the id of the template we want to update
     * @param array $data with the following keys and values
     *      'responseURL' => redirect URL if used as an action in a form.
     *      'callback' => (string) the callback function if called as JSONP.
     * @return string
     * @access public
    """
    def uploadTemplate(self, id, data = {}):
        
        url = str(self._options['docxpressoInstallation']) + '/documents/upload_template/' + str(id)
        
        #we build and options object
        options = {}
        if not(self.empty(data,'responseURL')) :
            options['responseURL'] = data['responseURL']
        
        if not(self.empty(data,'callback')) :
            options['callback'] = data['callback']
        
       
        opt = self.base64_encode_url_safe(json.dumps(options, separators=(',', ':')))
        return self._returnLink(url, id, opt)
    


    """
     * Returns a link to resend pending webhooks.
     * 
     * @param string $callback the callback name that we want to use for padded
     * JSON responses. If empty plain JSON will be returned.
     * @return string
     * @access public
    """ 
    def managePendingWebhooks(self, callback = ''):
      
        url = str(self._options['docxpressoInstallation']) + '/data/webhook/pending'

        if (callback != '' and callback != None) :
            url += '/' + str(callback)
        

        return self ._returnLink(url)
    



    """
     * Creates the link requested by all other methods
     * 
     * @param string $url
     * @param mixed $id
     * @param mixed $opt
     * @return string
     * @access private
     """
    def _returnLink(self, url, id=None, opt=None):
        
        uniqid = self.generate_uniqid()
        timestamp = int(time.time())
        control = ''
        if (id!=None):
            control +=  str(id) + '-'
        control += str(timestamp) + '-' + str(uniqid)
        if (opt!=None):
            control += '-' + str(opt)
        
        masterKey = bytes(self._options['pKey'], 'UTF-8')
        pbHash = hashlib.sha1(control.encode()).digest()
        APIKEY = hmac.new(masterKey, pbHash, hashlib.sha1).hexdigest()

        addr = url + '?'
        addr += 'timestamp=' + str(timestamp) +'&'
        addr += 'uniqid=' + str(uniqid) + '&'
        addr += 'APIKEY=' + str(APIKEY)

        if(opt!=None):
            addr+= '&options=' + opt
        
        return addr

    """
    *********************************************/
    /*               ACCESS CONTROL              */
    /*      For data exchange with Docxpresso    */
    /*********************************************/ 
    
    /**
     * Whenever interacting with Docxpresso via a requestDataURI or 
     * responseDataURI parameters of the documentPreview method there
     * is an APIKEY based on HMAC that allows to identify petitions as
     * legitimate.
     * This method simplifies the task to check if the request is legitimate
     * by returning a boolean value: true for authorized requests and false
     * otherwise
     * 
     * @param string $data the POST/GET variable data sent along with 
     * the request
     * @param string $timestamp the POST/GET variable timestamp sent along with 
     * the request
     * @param string $uniqid the POST/GET variable uniqid sent along with 
     * the request
     * @param string $APIKEY the POST/GET variable APIKEY sent along with 
     * the request
     * @return boolean
     * @access public
     """
    def checkAPIKEY(self, data, timestamp, uniqid, APIKEY) :
    
        masterKey = bytes(self._options['pKey'], 'UTF-8')
        forward = hashlib.sha1((timestamp + '-' + uniqid + '-' + data).encode()).digest()
        refAPIKEY = hmac.new(masterKey, forward, hashlib.sha1).hexdigest()
        
        if (refAPIKEY == APIKEY):
            return True
        else:
            return False
        
    
    """
     * Whenever sending a request to an external API service the timestamp
     * and a service token are added to the query parameters.
     * 
     * This method checks that the pair timestamp and token where generated
     * from the given Docxpresso installation
     * 
     * @param string $timestamp the GET variable timestamp sent along with 
     * the request
     * @param string $token the GET variable uniqid sent along with 
     * the request
     * @param integer $expires number of seconds before the token expires. 
     * Default value is 3600.
     * @return boolean
     * @access public
    """
    def checkServiceToken(self, timestamp, token, expires = 3600):
    
        currentTime = int(time.time())
        myTime =  int(timestamp)
        if ((currentTime - myTime) > expires):
            return False
        
        masterKey = bytes(self._options['pKey'], 'UTF-8')
        forward = hashlib.sha1((timestamp + masterKey + timestamp).encode()).digest()
        refToken = hmac.new(masterKey, forward, hashlib.sha1).hexdigest()
    
        if (refToken == token):
            return True
        else :
            return False
        
    

    def _generateOTP (self):
        random = int(math.floor(random.randint(99999,99999999)))
        timestamp =  int(time.time())

        byte_pkey = bytes(self._options['pKey'], 'UTF-8')
        raw = (hmac.new( byte_pkey, ('otp' + random + '_' + timestamp + 'A random sentence').encode(), hashlib.sha1 )).hexdigest()
        return raw.substr(6, 12)
    
    
    def empty (self, data, prop):
        if (data == '' or data == None or data  == 0) or data.get(prop)==None or (prop == None or prop == '' or prop == 0):
            return True 
        else:
            return False
     

    def isset (self, data, prop):
        if type (data) != 'undefined' and data.get(prop)!=None and (prop != None or prop != '' or prop != 0):
            return True
        else:
          return False
      

    def generate_uniqid(self):
            return int(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) + int(math.floor(random.randint(99999,99999999)))
    
    





 

