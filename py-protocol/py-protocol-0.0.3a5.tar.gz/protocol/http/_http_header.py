import typing as t

class T_Element(object):
    def __init__(self, name, value: str|t.Iterable[str]|int= None) -> None:
        self.__value__ = value
        self.__name__ = name

    def __str__(self) -> str:
        if type(self.__value__) is str:
            return f'{self.__name__}: {self.__value__}\r\n' if self.__value__ else ""
        elif type(self.__value__) is int:
            return f'{self.__name__}: {str(self.__value__)}\r\n'
        return '\r\n'.join([f'{self.__name__}: {i}' for i in self.__value__]) + '\r\n'

    def append(self, _v: str|t.Iterable[str]):
        tmp = self.__value__
        self.__value__ = []
        if tmp:
            if type(tmp) is str:
                self.__value__.append(tmp)
            else:
                self.__value__.extend(tmp)
        if type(_v) is str:
            self.__value__.append(_v)
        else:
            self.__value__.extend(_v)

    @property
    def value(self) -> t.Optional[str|t.Iterable[str]]:
        return self.__value__
    @value.setter
    def value(self, _v):
        self.__value__ = _v
    
    @property
    def name(self) -> t.Optional[str]:
        return self.__name__
    @name.setter
    def name(self, _n : t.Optional[str]) -> None:
        self.__name__ = _n 

class T_HTTPHeader:
    def __init__(
            self, 
            _vHeader : t.Optional[str|dict[str, str]|t.Iterable[str]] = None
        ) -> None:
        self.__accept__ = T_Element('Accept')
        self.__accept_ch__ = T_Element('Accept-CH')
        self.__accept_ch_lifetime__ = T_Element('Accept-CH-Lifetime')
        self.__accept_charset__ = T_Element('Accept-Charset')
        self.__accept_encoding__ = T_Element('Accept-Encoding')
        self.__accept_language__ = T_Element('Accept-Language')
        self.__accept_patch__ = T_Element('Accept-Patch')
        self.__accept_post__ = T_Element('Accept-Post')
        self.__accept_ranges__ = T_Element('Accept-Ranges')
        self.__access_control_allow_credentials__ = T_Element('Access-Control-Allow-Credentials')
        self.__access_control_allow_headers__ = T_Element('Access-Control-Allow-Headers')
        self.__access_control_allow_methods__ = T_Element('Access-Control-Allow-Methods')
        self.__access_control_allow_origin__ = T_Element('Access-Control-Allow-Origin')
        self.__access_control_expose_headers__ = T_Element('Access-Control-Expose-Headers')
        self.__access_control_max_age__ = T_Element('Access-Control-Max-Age')
        self.__access_control_request_headers__ = T_Element('Access-Control-Request-Headers')
        self.__access_control_request_method__ = T_Element('Access-Control-Request-Method')
        self.__age__ = T_Element('Age')
        self.__allow__ = T_Element('Allow')
        self.__alt_svc__ = T_Element('Alt-Svc')
        self.__authorization__ = T_Element('Authorization')
        self.__cache_control__ = T_Element('Cache-Control')
        self.__clear_site_data__ = T_Element('Clear-Site-Data')
        self.__connection__ = T_Element('Connection')
        self.__content_disposition__ = T_Element('Content-Disposition')
        self.__content_dpr__ = T_Element('Content-DPR')
        self.__content_encoding__ = T_Element('Content-Encoding')
        self.__content_language__ = T_Element('Content-Language')
        self.__content_length__ = T_Element('Content-Length')
        self.__content_location__ = T_Element('Content-Location')
        self.__content_range__ = T_Element('Content-Range')
        self.__content_security_policy__ = T_Element('Content-Security-Policy')
        self.__content_security_policy_report_only__ = T_Element('Content-Security-Policy-Report-Only')
        self.__content_type__ = T_Element('Content-Type')
        self.__cookie__ = T_Element('Cookie')
        self.__cross_origin_embedder_policy__ = T_Element('Cross-Origin-Embedder-Policy')
        self.__cross_origin_opener_policy__ = T_Element('Cross-Origin-Opener-Policy')
        self.__cross_origin_resource_policy__ = T_Element('Cross-Origin-Resource-Policy')
        self.__date__ = T_Element('Date')
        self.__device_memory__ = T_Element('Device-Memory')
        self.__digest__ = T_Element('Digest')
        self.__dnt__ = T_Element('DNT')
        self.__downlink__ = T_Element('Downlink')
        self.__dpr__ = T_Element('DPR')
        self.__early_data__ = T_Element('Early-Data')
        self.__ect__ = T_Element('ECT')
        self.__etag__ = T_Element('ETag')
        self.__expect__ = T_Element('Expect')
        self.__expect_ct__ = T_Element('Expect-CT')
        self.__expires__ = T_Element('Expires')
        self.__feature_policy__ = T_Element('Feature-Policy')
        self.__forwarded__ = T_Element('Forwarded')
        self.__from__ = T_Element('From')
        self.__host__ = T_Element('Host')
        self.__if_match__ = T_Element('If-Match')
        self.__if_modified_since__ = T_Element('If-Modified-Since')
        self.__if_none_match__ = T_Element('If-None-Match')
        self.__if_range__ = T_Element('If-Range')
        self.__if_unmodified_since__ = T_Element('If-Unmodified-Since')
        self.__keep_alive__ = T_Element('Keep-Alive')
        self.__large_allocation__ = T_Element('Large-Allocation')
        self.__last_modified__ = T_Element('Last-Modified')
        self.__link__ = T_Element('Link')
        self.__location__ = T_Element('Location')
        self.__max_forwards__ = T_Element('Max-Forwards')
        self.__nel__ = T_Element('NEL')
        self.__origin__ = T_Element('Origin')
        self.__pragma__ = T_Element('Pragma')
        self.__proxy_authenticate__ = T_Element('Proxy-Authenticate')
        self.__proxy_authorization__ = T_Element('Proxy-Authorization')
        self.__range__ = T_Element('Range')
        self.__referer__ = T_Element('Referer')
        self.__referrer_policy__ = T_Element('Referrer-Policy')
        self.__retry_after__ = T_Element('Retry-After')
        self.__rtt__ = T_Element('RTT')
        self.__save_data__ = T_Element('Save-Data')
        self.__sec_ch_ua__ = T_Element('Sec-CH-UA')
        self.__sec_ch_ua_arch__ = T_Element('Sec-CH-UA-Arch')
        self.__sec_ch_ua_bitness__ = T_Element('Sec-CH-UA-Bitness')
        self.__sec_ch_ua_full_version__ = T_Element('Sec-CH-UA-Full-Version')
        self.__sec_ch_ua_full_version_list__ = T_Element('Sec-CH-UA-Full-Version-List')
        self.__sec_ch_ua_mobile__ = T_Element('Sec-CH-UA-Mobile')
        self.__sec_ch_ua_model__ = T_Element('Sec-CH-UA-Model')
        self.__sec_ch_ua_platform__ = T_Element('Sec-CH-UA-Platform')
        self.__sec_ch_ua_platform_version__ = T_Element('Sec-CH-UA-Platform-Version')
        self.__sec_fetch_dest__ = T_Element('Sec-Fetch-Dest')
        self.__sec_fetch_mode__ = T_Element('Sec-Fetch-Mode')
        self.__sec_fetch_site__ = T_Element('Sec-Fetch-Site')
        self.__sec_fetch_user__ = T_Element('Sec-Fetch-User')
        self.__sec_gpc__    = T_Element('Sec-GPC')
        self.__sec_websocket_accept__ = T_Element('Sec-WebSocket-Accept')
        self.__server__ = T_Element('Server')
        self.__server_timing__ = T_Element('Server-Timing')
        self.__service_worker_navigation_preload__ = T_Element('Service-Worker-Navigation-Preload')
        self.__set_cookie__ = T_Element('Set-Cookie')
        self.__sourcemap__ = T_Element('SourceMap')
        self.__strict_transport_security__ = T_Element('Strict-Transport-Security')
        self.__te__ = T_Element('TE')
        self.__timing_allow_origin__ = T_Element('Timing-Allow-Origin')
        self.__tk__ = T_Element('TK')
        self.__trailer__ = T_Element('Trailer')
        self.__transfer_encoding__ = T_Element('Transfer-Encoding')
        self.__upgrade_insecure_requests__ = T_Element('Upgrade-Insecure-Requests')
        self.__user_agent__ = T_Element('User-Agent')
        self.__vary__ = T_Element('Vary')
        self.__via__ = T_Element('Via')
        self.__viewport_width__ = T_Element('Viewport-Width')
        self.__want_digest__ = T_Element('Want-Digest')
        self.__warning__ = T_Element('Warning')
        self.__width__ = T_Element('Width')
        self.__www_authenticate__ = T_Element('WWW-Authenticate')
        self.__x_content_type_options__ = T_Element('X-Content-Type-Options')
        self.__x_dns_prefetch_control__ = T_Element('X-DNS-Prefetch-Control')
        self.__x_forwarded_for__ = T_Element('X-Forwarded-For')
        self.__x_forwarded_host__ = T_Element('X-Forwarded-Host')
        self.__x_forwarded_proto__ = T_Element('X-Forwarded-Proto')
        self.__x_frame_options__ = T_Element('X-Frame-Options')
        self.__x_xss_protection__ = T_Element('X-XSS-Protection')

        if type(_vHeader) is str:
            __tmp__ = _vHeader.split('\r\n')
            for i in __tmp__:
                __tmp1__ = i.split(': ')
                if len(__tmp1__) == 2:
                    self.__dict__[f"__{__tmp1__[0].replace('-', '_').lower()}__"].value = __tmp1__[1]
        elif type(_vHeader) is dict[str, str]:
            for attributes in _vHeader:
                self.__dict__[f"__{attributes.replace('-', '_').lower()}__"].value = _vHeader[attributes]
        elif type(_vHeader) is t.Iterable[str]:
            for line in _vHeader:
                __tmp1__ = line.split(': ')
                if len(__tmp1__) == 2:
                    self.__dict__[f"__{__tmp1__[0].replace('-', '_').lower()}__"].value = __tmp1__[1]

    def __str__(self) -> str:
        re= ""
        for i in self.__dict__:
            if self.__dict__[i].value or type(self.__dict__[i].value) is int:
                re += self.__dict__[i].__str__()
        return re


    def changeInfo(self, _n : str | bytes, _v: t.Optional[str | bytes] = None) -> None:
        if type(_n) is bytes:
            _n = _n.decode()
        if type(_v) is bytes:
            _v = _v.decode()
        self.__dict__[f"__{_n.replace('-', '_').lower()}__"].value = _v

    @property
    def accept(self) -> T_Element:
        return self.__accept__
    @accept.setter
    def accept(self, _v) -> None:
        self.__accept__.value = _v
    def append_accept(self, _v: str|t.Iterable[str]):
        self.__accept__.append(_v)
    
    @property
    def accept_ch(self) -> T_Element:
        return self.__accept_ch__
    @accept_ch.setter
    def accept_ch(self, _v) -> None:
        self.__accept_ch__.value= _v
    def append_accept_ch(self, _v: str|t.Iterable[str]):
        self.__accept_ch__.append(_v)

    @property
    def accept_ch_lifetime(self) -> T_Element:
        return self.__accept_ch_lifetime__
    @accept_ch_lifetime.setter
    def accept_ch_lifetime(self, _v) -> None:
        self.__accept_ch_lifetime__.value= _v
    def append_accept_ch_lifetime(self, _v: str|t.Iterable[str]):
        self.__accept_ch_lifetime__.append(_v)

    @property
    def accept_charset(self) -> T_Element:
        return self.__accept_charset__
    @accept_charset.setter
    def accept_charset(self, _v) -> None:
        self.__accept_charset__.value= _v
    def append_accept_charset(self, _v: str|t.Iterable[str]):
        self.__accept_charset__.append(_v)

    @property
    def accept_encoding(self) -> T_Element:
        return self.__accept_encoding__
    @accept_encoding.setter
    def accept_encoding(self, _v) -> None:
        self.__accept_encoding__.value= _v
    def append_accept_encoding(self, _v: str|t.Iterable[str]):
        self.__accept_encoding__.append(_v)

    @property
    def accept_language(self) -> T_Element:
        return self.__accept_language__
    @accept_language.setter
    def accept_language(self, _v) -> None:
        self.__accept_language__.value= _v
    def append_accept_language(self, _v: str|t.Iterable[str]):
        self.__accept_language__.append(_v)

    @property
    def accept_patch(self) -> T_Element:
        return self.__accept_patch__
    @accept_patch.setter
    def accept_patch(self, _v) -> None:
        self.__accept_patch__.value= _v
    def append_accept_patch(self, _v: str|t.Iterable[str]):
        self.__accept_patch__.append(_v)
    
    @property
    def accept_post(self) -> T_Element:
        return self.__accept_post__
    @accept_post.setter
    def accept_post(self, _v) -> None:
        self.__accept_post__.value= _v
    def append_accept_post(self, _v: str|t.Iterable[str]):
        self.__accept_post__.append(_v)
        
    @property
    def accept_ranges(self) -> T_Element:
        return self.__accept_ranges__
    @accept_ranges.setter
    def accept_ranges(self, _v) -> None:
        self.__accept_ranges__.value= _v
    def append_accept_ranges(self, _v: str|t.Iterable[str]):
        self.__accept_ranges__.append(_v)
        
    @property
    def access_control_allow_credentials(self) -> T_Element:
        return self.__access_control_allow_credentials__
    @access_control_allow_credentials.setter
    def access_control_allow_credentials(self, _v) -> None:
        self.__access_control_allow_credentials__.value= _v
    def append_access_control_allow_credentials(self, _v: str|t.Iterable[str]):
        self.__access_control_allow_credentials__.append(_v)
        
    @property
    def access_control_allow_headers(self) -> T_Element:
        return self.__access_control_allow_headers__
    @access_control_allow_headers.setter
    def access_control_allow_headers(self, _v) -> None:
        self.__access_control_allow_headers__.value= _v
    def append_access_control_allow_headers(self, _v: str|t.Iterable[str]):
        self.__access_control_allow_headers__.append(_v)
        
    @property
    def access_control_allow_methods(self) -> T_Element:
        return self.__access_control_allow_methods__
    @access_control_allow_methods.setter
    def access_control_allow_methods(self, _v) -> None:
        self.__access_control_allow_methods__.value= _v
    def append_access_control_allow_methods(self, _v: str|t.Iterable[str]):
        self.__access_control_allow_methods__.append(_v)
        
    @property
    def access_control_allow_origin(self) -> T_Element:
        return self.__access_control_allow_origin__
    @access_control_allow_origin.setter
    def access_control_allow_origin(self, _v) -> None:
        self.__access_control_allow_origin__.value= _v
    def append_access_control_allow_origin(self, _v: str|t.Iterable[str]):
        self.__access_control_allow_origin__.append(_v)
        
    @property
    def access_control_expose_headers(self) -> T_Element:
        return self.__access_control_expose_headers__
    @access_control_expose_headers.setter
    def access_control_expose_headers(self, _v) -> None:
        self.__access_control_expose_headers__.value= _v
    def append_access_control_expose_headers(self, _v: str|t.Iterable[str]):
        self.__access_control_expose_headers__.append(_v)
        
    @property
    def access_control_max_age(self) -> T_Element:
        return self.__access_control_max_age__
    @access_control_max_age.setter
    def access_control_max_age(self, _v) -> None:
        self.__access_control_max_age__.value= _v
    def append_access_control_max_age(self, _v: str|t.Iterable[str]):
        self.__access_control_max_age__.append(_v)
        
    @property
    def access_control_request_headers(self) -> T_Element:
        return self.__access_control_request_headers__
    @access_control_request_headers.setter
    def access_control_request_headers(self, _v) -> None:
        self.__access_control_request_headers__.value= _v
    def append_access_control_request_headers(self, _v: str|t.Iterable[str]):
        self.__access_control_request_headers__.append(_v)
        
    @property
    def access_control_request_method(self) -> T_Element:
        return self.__access_control_request_method__
    @access_control_request_method.setter
    def access_control_request_method(self, _v) -> None:
        self.__access_control_request_method__.value= _v
    def append_access_control_request_method(self, _v: str|t.Iterable[str]):
        self.__access_control_request_method__.append(_v)
        
    @property
    def age(self) -> T_Element:
        return self.__age__
    @age.setter
    def age(self, _v) -> None:
        self.__age__.value= _v
    def append_age(self, _v: str|t.Iterable[str]):
        self.__age__.append(_v)
        
    @property
    def allow(self) -> T_Element:
        return self.__allow__
    @allow.setter
    def allow(self, _v) -> None:
        self.__allow__.value= _v
    def append_allow(self, _v: str|t.Iterable[str]):
        self.__allow__.append(_v)
        
    @property
    def alt_svc(self) -> T_Element:
        return self.__alt_svc__
    @alt_svc.setter
    def alt_svc(self, _v) -> None:
        self.__alt_svc__.value= _v
    def append_alt_svc(self, _v: str|t.Iterable[str]):
        self.__alt_svc__.append(_v)
        
    @property
    def authorization(self) -> T_Element:
        return self.__authorization__
    @authorization.setter
    def authorization(self, _v) -> None:
        self.__authorization__.value= _v
    def append_authorization(self, _v: str|t.Iterable[str]):
        self.__authorization__.append(_v)
        
    @property
    def cache_control(self) -> T_Element:
        return self.__cache_control__
    @cache_control.setter
    def cache_control(self, _v) -> None:
        self.__cache_control__.value= _v
    def append_cache_control(self, _v: str|t.Iterable[str]):
        self.__cache_control__.append(_v)
        
    @property
    def clear_site_data(self) -> T_Element:
        return self.__clear_site_data__
    @clear_site_data.setter
    def clear_site_data(self, _v) -> None:
        self.__clear_site_data__.value= _v
    def append_clear_site_data(self, _v: str|t.Iterable[str]):
        self.__clear_site_data__.append(_v)
        
    @property
    def connection(self) -> T_Element:
        return self.__connection__
    @connection.setter
    def connection(self, _v) -> None:
        self.__connection__.value= _v
    def append_connection(self, _v: str|t.Iterable[str]):
        self.__connection__.append(_v)
        
    @property
    def content_disposition(self) -> T_Element:
        return self.__content_disposition__
    @content_disposition.setter
    def content_disposition(self, _v) -> None:
        self.__content_disposition__.value= _v
    def append_content_disposition(self, _v: str|t.Iterable[str]):
        self.__content_disposition__.append(_v)
        
    @property
    def content_dpr(self) -> T_Element:
        return self.__content_dpr__
    @content_dpr.setter
    def content_dpr(self, _v) -> None:
        self.__content_dpr__.value= _v
    def append_content_dpr(self, _v: str|t.Iterable[str]):
        self.__content_dpr__.append(_v)
        
    @property
    def content_encoding(self) -> T_Element:
        return self.__content_encoding__
    @content_encoding.setter
    def content_encoding(self, _v) -> None:
        self.__content_encoding__.value= _v
    def append_content_encoding(self, _v: str|t.Iterable[str]):
        self.__content_encoding__.append(_v)
        
    @property
    def content_language(self) -> T_Element:
        return self.__content_language__
    @content_language.setter
    def content_language(self, _v) -> None:
        self.__content_language__.value= _v
    def append_content_language(self, _v: str|t.Iterable[str]):
        self.__content_language__.append(_v)
        
    @property
    def content_length(self) -> T_Element:
        return self.__content_length__
    @content_length.setter
    def content_length(self, _v) -> None:
        self.__content_length__.value= _v
    def append_content_length(self, _v: str|t.Iterable[str]):
        self.__content_length__.append(_v)
        
    @property
    def content_location(self) -> T_Element:
        return self.__content_location__
    @content_location.setter
    def content_location(self, _v) -> None:
        self.__content_location__.value= _v
    def append_content_location(self, _v: str|t.Iterable[str]):
        self.__content_location__.append(_v)
        
    @property
    def content_range(self) -> T_Element:
        return self.__content_range__
    @content_range.setter
    def content_range(self, _v) -> None:
        self.__content_range__.value= _v
    def append_content_range(self, _v: str|t.Iterable[str]):
        self.__content_range__.append(_v)
        
    @property
    def content_security_policy(self) -> T_Element:
        return self.__content_security_policy__
    @content_security_policy.setter
    def content_security_policy(self, _v) -> None:
        self.__content_security_policy__.value= _v
    def append_content_security_policy(self, _v: str|t.Iterable[str]):
        self.__content_security_policy__.append(_v)
        
    @property
    def content_security_policy_report_only(self) -> T_Element:
        return self.__content_security_policy_report_only__
    @content_security_policy_report_only.setter
    def content_security_policy_report_only(self, _v) -> None:
        self.__content_security_policy_report_only__.value= _v
    def append_content_security_policy_report_only(self, _v: str|t.Iterable[str]):
        self.__content_security_policy_report_only__.append(_v)
        
    @property
    def content_type(self) -> T_Element:
        return self.__content_type__
    @content_type.setter
    def content_type(self, _v) -> None:
        self.__content_type__.value= _v
    def append_content_type(self, _v: str|t.Iterable[str]):
        self.__content_type__.append(_v)
        
    @property
    def cookie(self) -> T_Element:
        return self.__cookie__
    @cookie.setter
    def cookie(self, _v) -> None:
        self.__cookie__.value= _v
    def append_cookie(self, _v: str|t.Iterable[str]):
        self.__cookie__.append(_v)
        
    @property
    def cross_origin_embedder_policy(self) -> T_Element:
        return self.__cross_origin_embedder_policy__
    @cross_origin_embedder_policy.setter
    def cross_origin_embedder_policy(self, _v) -> None:
        self.__cross_origin_embedder_policy__.value= _v
    def append_cross_origin_embedder_policy(self, _v: str|t.Iterable[str]):
        self.__cross_origin_embedder_policy__.append(_v)
        
    @property
    def cross_origin_opener_policy(self) -> T_Element:
        return self.__cross_origin_opener_policy__
    @cross_origin_opener_policy.setter
    def cross_origin_opener_policy(self, _v) -> None:
        self.__cross_origin_opener_policy__.value= _v
    def append_cross_origin_opener_policy(self, _v: str|t.Iterable[str]):
        self.__cross_origin_opener_policy__.append(_v)
        
    @property
    def cross_origin_resource_policy(self) -> T_Element:
        return self.__cross_origin_resource_policy__
    @cross_origin_resource_policy.setter
    def cross_origin_resource_policy(self, _v) -> None:
        self.__cross_origin_resource_policy__.value= _v
    def append_cross_origin_resource_policy(self, _v: str|t.Iterable[str]):
        self.__cross_origin_resource_policy__.append(_v)
        
    @property
    def date(self) -> T_Element:
        return self.__date__
    @date.setter
    def date(self, _v) -> None:
        self.__date__.value= _v
    def append_date(self, _v: str|t.Iterable[str]):
        self.__date__.append(_v)
        
    @property
    def device_memory(self) -> T_Element:
        return self.__device_memory__
    @device_memory.setter
    def device_memory(self, _v) -> None:
        self.__device_memory__.value= _v
    def append_device_memory(self, _v: str|t.Iterable[str]):
        self.__device_memory__.append(_v)
        
    @property
    def digest(self) -> T_Element:
        return self.__digest__
    @digest.setter
    def digest(self, _v) -> None:
        self.__digest__.value= _v
    def append_digest(self, _v: str|t.Iterable[str]):
        self.__digest__.append(_v)
        
    @property
    def dnt(self) -> T_Element:
        return self.__dnt__
    @dnt.setter
    def dnt(self, _v) -> None:
        self.__dnt__.value= _v
    def append_dnt(self, _v: str|t.Iterable[str]):
        self.__dnt__.append(_v)
        
    @property
    def downlink(self) -> T_Element:
        return self.__downlink__
    @downlink.setter
    def downlink(self, _v) -> None:
        self.__downlink__.value= _v
    def append_downlink(self, _v: str|t.Iterable[str]):
        self.__downlink__.append(_v)
        
    @property
    def dpr(self) -> T_Element:
        return self.__dpr__
    @dpr.setter
    def dpr(self, _v) -> None:
        self.__dpr__.value= _v
    def append_dpr(self, _v: str|t.Iterable[str]):
        self.__dpr__.append(_v)
        
    @property
    def early_data(self) -> T_Element:
        return self.__early_data__
    @early_data.setter
    def early_data(self, _v) -> None:
        self.__early_data__.value= _v
    def append_early_data(self, _v: str|t.Iterable[str]):
        self.__early_data__.append(_v)
        
    @property
    def ect(self) -> T_Element:
        return self.__ect__
    @ect.setter
    def ect(self, _v) -> None:
        self.__ect__.value= _v
    def append_ect(self, _v: str|t.Iterable[str]):
        self.__ect__.append(_v)
        
    @property
    def etag(self) -> T_Element:
        return self.__etag__
    @etag.setter
    def etag(self, _v) -> None:
        self.__etag__.value= _v
    def append_etag(self, _v: str|t.Iterable[str]):
        self.__etag__.append(_v)
        
    @property
    def expect(self) -> T_Element:
        return self.__expect__
    @expect.setter
    def expect(self, _v) -> None:
        self.__expect__.value= _v
    def append_expect(self, _v: str|t.Iterable[str]):
        self.__expect__.append(_v)
        
    @property
    def expect_ct(self) -> T_Element:
        return self.__expect_ct__
    @expect_ct.setter
    def expect_ct(self, _v) -> None:
        self.__expect_ct__.value= _v
    def append_expect_ct(self, _v: str|t.Iterable[str]):
        self.__expect_ct__.append(_v)
        
    @property
    def expires(self) -> T_Element:
        return self.__expires__
    @expires.setter
    def expires(self, _v) -> None:
        self.__expires__.value= _v
    def append_expires(self, _v: str|t.Iterable[str]):
        self.__expires__.append(_v)
        
    @property
    def feature_policy(self) -> T_Element:
        return self.__feature_policy__
    @feature_policy.setter
    def feature_policy(self, _v) -> None:
        self.__feature_policy__.value= _v
    def append_feature_policy(self, _v: str|t.Iterable[str]):
        self.__feature_policy__.append(_v)
        
    @property
    def forwarded(self) -> T_Element:
        return self.__forwarded__
    @forwarded.setter
    def forwarded(self, _v) -> None:
        self.__forwarded__.value= _v
    def append_forwarded(self, _v: str|t.Iterable[str]):
        self.__forwarded__.append(_v)
        
    @property
    def _from(self) -> T_Element:
        return self.__from__
    @_from.setter
    def _from(self, _v) -> None:
        self.__from__.value= _v
    def append_from(self, _v: str|t.Iterable[str]):
        self.__from__.append(_v)
        
    @property
    def host(self) -> T_Element:
        return self.__host__
    @host.setter
    def host(self, _v) -> None:
        self.__host__.value= _v
    def append_host(self, _v: str|t.Iterable[str]):
        self.__host__.append(_v)
        
    @property
    def if_match(self) -> T_Element:
        return self.__if_match__
    @if_match.setter
    def if_match(self, _v) -> None:
        self.__if_match__.value= _v
    def append_if_match(self, _v: str|t.Iterable[str]):
        self.__if_match__.append(_v)
        
    @property
    def if_modified_since(self) -> T_Element:
        return self.__if_modified_since__
    @if_modified_since.setter
    def if_modified_since(self, _v) -> None:
        self.__if_modified_since__.value= _v
    def append_if_modified_since(self, _v: str|t.Iterable[str]):
        self.__if_modified_since__.append(_v)
        
    @property
    def if_none_match(self) -> T_Element:
        return self.__if_none_match__
    @if_none_match.setter
    def if_none_match(self, _v) -> None:
        self.__if_none_match__.value= _v
    def append_if_none_match(self, _v: str|t.Iterable[str]):
        self.__if_none_match__.append(_v)
        
    @property
    def if_range(self) -> T_Element:
        return self.__if_range__
    @if_range.setter
    def if_range(self, _v) -> None:
        self.__if_range__.value= _v
    def append_if_range(self, _v: str|t.Iterable[str]):
        self.__if_range__.append(_v)
        
    @property
    def if_unmodified_since(self) -> T_Element:
        return self.__if_unmodified_since__
    @if_unmodified_since.setter
    def if_unmodified_since(self, _v) -> None:
        self.__if_unmodified_since__.value= _v
    def append_if_unmodified_since(self, _v: str|t.Iterable[str]):
        self.__if_unmodified_since__.append(_v)
        
    @property
    def keep_alive(self) -> T_Element:
        return self.__keep_alive__
    @keep_alive.setter
    def keep_alive(self, _v) -> None:
        self.__keep_alive__.value= _v
    def append_keep_alive(self, _v: str|t.Iterable[str]):
        self.__keep_alive__.append(_v)
        
    @property
    def large_allocation(self) -> T_Element:
        return self.__large_allocation__
    @large_allocation.setter
    def large_allocation(self, _v) -> None:
        self.__large_allocation__.value= _v
    def append_large_allocation(self, _v: str|t.Iterable[str]):
        self.__large_allocation__.append(_v)
        
    @property
    def last_modified(self) -> T_Element:
        return self.__last_modified__
    @last_modified.setter
    def last_modified(self, _v) -> None:
        self.__last_modified__.value= _v
    def append_last_modified(self, _v: str|t.Iterable[str]):
        self.__last_modified__.append(_v)
        
    @property
    def link(self) -> T_Element:
        return self.__link__
    @link.setter
    def link(self, _v) -> None:
        self.__link__.value= _v
    def append_link(self, _v: str|t.Iterable[str]):
        self.__link__.append(_v)
        
    @property
    def location(self) -> T_Element:
        return self.__location__
    @location.setter
    def location(self, _v) -> None:
        self.__location__.value= _v
    def append_location(self, _v: str|t.Iterable[str]):
        self.__location__.append(_v)
        
    @property
    def max_forwards(self) -> T_Element:
        return self.__max_forwards__
    @max_forwards.setter
    def max_forwards(self, _v) -> None:
        self.__max_forwards__.value= _v
    def append_max_forwards(self, _v: str|t.Iterable[str]):
        self.__max_forwards__.append(_v)
        
    @property
    def nel(self) -> T_Element:
        return self.__nel__
    @nel.setter
    def nel(self, _v) -> None:
        self.__nel__.value= _v
    def append_nel(self, _v: str|t.Iterable[str]):
        self.__nel__.append(_v)
        
    @property
    def origin(self) -> T_Element:
        return self.__origin__
    @origin.setter
    def origin(self, _v) -> None:
        self.__origin__.value= _v
    def append_origin(self, _v: str|t.Iterable[str]):
        self.__origin__.append(_v)
        
    @property
    def pragma(self) -> T_Element:
        return self.__pragma__
    @pragma.setter
    def pragma(self, _v) -> None:
        self.__pragma__.value= _v
    def append_pragma(self, _v: str|t.Iterable[str]):
        self.__pragma__.append(_v)

    @property
    def proxy_authenticate(self) -> T_Element:
        return self.__proxy_authenticate__
    @proxy_authenticate.setter
    def proxy_authenticate(self, _v) -> None:
        self.__proxy_authenticate__.value= _v
    def append_proxy_authenticate(self, _v: str|t.Iterable[str]):
        self.__proxy_authenticate__.append(_v)

    @property
    def proxy_authorization(self) -> T_Element:
        return self.__proxy_authorization__
    @proxy_authorization.setter
    def proxy_authorization(self, _v) -> None:
        self.__proxy_authorization__.value= _v
    def append_proxy_authorization(self, _v: str|t.Iterable[str]):
        self.__proxy_authorization__.append(_v)

    @property
    def range(self) -> T_Element:
        return self.__range__
    @range.setter
    def range(self, _v) -> None:
        self.__range__.value= _v
    def append_range(self, _v: str|t.Iterable[str]):
        self.__range__.append(_v)

    @property
    def referer(self) -> T_Element:
        return self.__referer__
    @referer.setter
    def referer(self, _v) -> None:
        self.__referer__.value= _v
    def append_referer(self, _v: str|t.Iterable[str]):
        self.__referer__.append(_v)

    @property
    def referrer_policy(self) -> T_Element:
        return self.__referrer_policy__
    @referrer_policy.setter
    def referrer_policy(self, _v) -> None:
        self.__referrer_policy__.value= _v
    def append_referrer_policy(self, _v: str|t.Iterable[str]):
        self.__referrer_policy__.append(_v)

    @property
    def retry_after(self) -> T_Element:
        return self.__retry_after__
    @retry_after.setter
    def retry_after(self, _v) -> None:
        self.__retry_after__.value= _v
    def append_retry_after(self, _v: str|t.Iterable[str]):
        self.__retry_after__.append(_v)

    @property
    def rtt(self) -> T_Element:
        return self.__rtt__
    @rtt.setter
    def rtt(self, _v) -> None:
        self.__rtt__.value= _v
    def append_rtt(self, _v: str|t.Iterable[str]):
        self.__rtt__.append(_v)

    @property
    def save_data(self) -> T_Element:
        return self.__save_data__
    @save_data.setter
    def save_data(self, _v) -> None:
        self.__save_data__.value= _v
    def append_save_data(self, _v: str|t.Iterable[str]):
        self.__save_data__.append(_v)

    @property
    def sec_ch_ua(self) -> T_Element:
        return self.__sec_ch_ua__
    @sec_ch_ua.setter
    def sec_ch_ua(self, _v) -> None:
        self.__sec_ch_ua__.value= _v
    def append_sec_ch_ua(self, _v: str|t.Iterable[str]):
        self.__sec_ch_ua__.append(_v)

    @property
    def sec_ch_ua_arch(self) -> T_Element:
        return self.__sec_ch_ua_arch__
    @sec_ch_ua_arch.setter
    def sec_ch_ua_arch(self, _v) -> None:
        self.__sec_ch_ua_arch__.value= _v
    def append_sec_ch_ua_arch(self, _v: str|t.Iterable[str]):
        self.__sec_ch_ua_arch__.append(_v)

    @property
    def sec_ch_ua_bitness(self) -> T_Element:
        return self.__sec_ch_ua_bitness__
    @sec_ch_ua_bitness.setter
    def sec_ch_ua_bitness(self, _v) -> None:
        self.__sec_ch_ua_bitness__.value= _v
    def append_sec_ch_ua_bitness(self, _v: str|t.Iterable[str]):
        self.__sec_ch_ua_bitness__.append(_v)

    @property
    def sec_ch_ua_full_version(self) -> T_Element:
        return self.__sec_ch_ua_full_version__
    @sec_ch_ua_full_version.setter
    def sec_ch_ua_full_version(self, _v) -> None:
        self.__sec_ch_ua_full_version__.value= _v
    def append_sec_ch_ua_full_version(self, _v: str|t.Iterable[str]):
        self.__sec_ch_ua_full_version__.append(_v)

    @property
    def sec_ch_ua_full_version_list(self) -> T_Element:
        return self.__sec_ch_ua_full_version_list__
    @sec_ch_ua_full_version_list.setter
    def sec_ch_ua_full_version_list(self, _v) -> None:
        self.__sec_ch_ua_full_version_list__.value= _v
    def append_sec_ch_ua_full_version_list(self, _v: str|t.Iterable[str]):
        self.__sec_ch_ua_full_version_list__.append(_v)

    @property
    def sec_ch_ua_mobile(self) -> T_Element:
        return self.__sec_ch_ua_mobile__
    @sec_ch_ua_mobile.setter
    def sec_ch_ua_mobile(self, _v) -> None:
        self.__sec_ch_ua_mobile__.value= _v
    def append_sec_ch_ua_mobile(self, _v: str|t.Iterable[str]):
        self.__sec_ch_ua_mobile__.append(_v)

    @property
    def sec_ch_ua_model(self) -> T_Element:
        return self.__sec_ch_ua_model__
    @sec_ch_ua_model.setter
    def sec_ch_ua_model(self, _v) -> None:
        self.__sec_ch_ua_model__.value= _v
    def append_sec_ch_ua_model(self, _v: str|t.Iterable[str]):
        self.__sec_ch_ua_model__.append(_v)

    @property
    def sec_ch_ua_platform(self) -> T_Element:
        return self.__sec_ch_ua_platform__
    @sec_ch_ua_platform.setter
    def sec_ch_ua_platform(self, _v) -> None:
        self.__sec_ch_ua_platform__.value= _v
    def append_sec_ch_ua_platform(self, _v: str|t.Iterable[str]):
        self.__sec_ch_ua_platform__.append(_v)

    @property
    def sec_ch_ua_platform_version(self) -> T_Element:
        return self.__sec_ch_ua_platform_version__
    @sec_ch_ua_platform_version.setter
    def sec_ch_ua_platform_version(self, _v) -> None:
        self.__sec_ch_ua_platform_version__.value= _v
    def append_sec_ch_ua_platform_version(self, _v: str|t.Iterable[str]):
        self.__sec_ch_ua_platform_version__.append(_v)

    @property
    def sec_fetch_dest(self) -> T_Element:
        return self.__sec_fetch_dest__
    @sec_fetch_dest.setter
    def sec_fetch_dest(self, _v) -> None:
        self.__sec_fetch_dest__.value= _v
    def append_sec_fetch_dest(self, _v: str|t.Iterable[str]):
        self.__sec_fetch_dest__.append(_v)

    @property
    def sec_fetch_mode(self) -> T_Element:
        return self.__sec_fetch_mode__
    @sec_fetch_mode.setter
    def sec_fetch_mode(self, _v) -> None:
        self.__sec_fetch_mode__.value= _v
    def append_sec_fetch_mode(self, _v: str|t.Iterable[str]):
        self.__sec_fetch_mode__.append(_v)

    @property
    def sec_fetch_site(self) -> T_Element:
        return self.__sec_fetch_site__
    @sec_fetch_site.setter
    def sec_fetch_site(self, _v) -> None:
        self.__sec_fetch_site__.value= _v
    def append_sec_fetch_site(self, _v: str|t.Iterable[str]):
        self.__sec_fetch_site__.append(_v)

    @property
    def sec_fetch_user(self) -> T_Element:
        return self.__sec_fetch_user__
    @sec_fetch_user.setter
    def sec_fetch_user(self, _v) -> None:
        self.__sec_fetch_user__.value= _v
    def append_sec_fetch_user(self, _v: str|t.Iterable[str]):
        self.__sec_fetch_user__.append(_v)

    @property
    def sec_gpc(self) -> T_Element:
        return self.__sec_gpc__
    @sec_gpc.setter
    def sec_gpc(self, _v) -> None:
        self.__sec_gpc__.value= _v
    def append_sec_gpc(self, _v: str|t.Iterable[str]):
        self.__sec_gpc__.append(_v)

    @property
    def sec_websocket_accept(self) -> T_Element:
        return self.__sec_websocket_accept__
    @sec_websocket_accept.setter
    def sec_websocket_accept(self, _v) -> None:
        self.__sec_websocket_accept__.value= _v
    def append_sec_websocket_accept(self, _v: str|t.Iterable[str]):
        self.__sec_websocket_accept__.append(_v)

    @property
    def server(self) -> T_Element:
        return self.__server__
    @server.setter
    def server(self, _v) -> None:
        self.__server__.value= _v
    def append_server(self, _v: str|t.Iterable[str]):
        self.__server__.append(_v)

    @property
    def server_timing(self) -> T_Element:
        return self.__server_timing__
    @server_timing.setter
    def server_timing(self, _v) -> None:
        self.__server_timing__.value= _v
    def append_server_timing(self, _v: str|t.Iterable[str]):
        self.__server_timing__.append(_v)

    @property
    def service_worker_navigation_preload(self) -> T_Element:
        return self.__service_worker_navigation_preload__
    @service_worker_navigation_preload.setter
    def service_worker_navigation_preload(self, _v) -> None:
        self.__service_worker_navigation_preload__.value= _v
    def append_service_worker_navigation_preload(self, _v: str|t.Iterable[str]):
        self.__service_worker_navigation_preload__.append(_v)

    @property
    def set_cookie(self) -> T_Element:
        return self.__set_cookie__
    @set_cookie.setter
    def set_cookie(self, _v) -> None:
        self.__set_cookie__.value= _v
    def append_set_cookie(self, _v: str|t.Iterable[str]):
        self.__set_cookie__.append(_v)

    @property
    def sourcemap(self) -> T_Element:
        return self.__sourcemap__
    @sourcemap.setter
    def sourcemap(self, _v) -> None:
        self.__sourcemap__.value= _v
    def append_sourcemap(self, _v: str|t.Iterable[str]):
        self.__sourcemap__.append(_v)

    @property
    def strict_transport_security(self) -> T_Element:
        return self.__strict_transport_security__
    @strict_transport_security.setter
    def strict_transport_security(self, _v) -> None:
        self.__strict_transport_security__.value= _v
    def append_strict_transport_security(self, _v: str|t.Iterable[str]):
        self.__strict_transport_security__.append(_v)

    @property
    def te(self) -> T_Element:
        return self.__te__
    @te.setter
    def te(self, _v) -> None:
        self.__te__.value= _v
    def append_te(self, _v: str|t.Iterable[str]):
        self.__te__.append(_v)

    @property
    def timing_allow_origin(self) -> T_Element:
        return self.__timing_allow_origin__
    @timing_allow_origin.setter
    def timing_allow_origin(self, _v) -> None:
        self.__timing_allow_origin__.value= _v
    def append_timing_allow_origin(self, _v: str|t.Iterable[str]):
        self.__timing_allow_origin__.append(_v)

    @property
    def tk(self) -> T_Element:
        return self.__tk__
    @tk.setter
    def tk(self, _v) -> None:
        self.__tk__.value= _v
    def append_tk(self, _v: str|t.Iterable[str]):
        self.__tk__.append(_v)

    @property
    def trailer(self) -> T_Element:
        return self.__trailer__
    @trailer.setter
    def trailer(self, _v) -> None:
        self.__trailer__.value= _v
    def append_trailer(self, _v: str|t.Iterable[str]):
        self.__trailer__.append(_v)

    @property
    def transfer_encoding(self) -> T_Element:
        return self.__transfer_encoding__
    @transfer_encoding.setter
    def transfer_encoding(self, _v) -> None:
        self.__transfer_encoding__.value= _v
    def append_transfer_encoding(self, _v: str|t.Iterable[str]):
        self.__transfer_encoding__.append(_v)

    @property
    def upgrade_insecure_requests(self) -> T_Element:
        return self.__upgrade_insecure_requests__
    @upgrade_insecure_requests.setter
    def upgrade_insecure_requests(self, _v) -> None:
        self.__upgrade_insecure_requests__.value= _v
    def append_upgrade_insecure_requests(self, _v: str|t.Iterable[str]):
        self.__upgrade_insecure_requests__.append(_v)

    @property
    def user_agent(self) -> T_Element:
        return self.__user_agent__
    @user_agent.setter
    def user_agent(self, _v) -> None:
        self.__user_agent__.value= _v
    def append_user_agent(self, _v: str|t.Iterable[str]):
        self.__user_agent__.append(_v)

    @property
    def vary(self) -> T_Element:
        return self.__vary__
    @vary.setter
    def vary(self, _v) -> None:
        self.__vary__.value= _v
    def append_vary(self, _v: str|t.Iterable[str]):
        self.__vary__.append(_v)

    @property
    def via(self) -> T_Element:
        return self.__via__
    @via.setter
    def via(self, _v) -> None:
        self.__via__.value= _v
    def append_via(self, _v: str|t.Iterable[str]):
        self.__via__.append(_v)

    @property
    def viewport_width(self) -> T_Element:
        return self.__viewport_width__
    @viewport_width.setter
    def viewport_width(self, _v) -> None:
        self.__viewport_width__.value= _v
    def append_viewport_width(self, _v: str|t.Iterable[str]):
        self.__viewport_width__.append(_v)

    @property
    def want_digest(self) -> T_Element:
        return self.__want_digest__
    @want_digest.setter
    def want_digest(self, _v) -> None:
        self.__want_digest__.value= _v
    def append_want_digest(self, _v: str|t.Iterable[str]):
        self.__want_digest__.append(_v)

    @property
    def warning(self) -> T_Element:
        return self.__warning__
    @warning.setter
    def warning(self, _v) -> None:
        self.__warning__.value= _v
    def append_warning(self, _v: str|t.Iterable[str]):
        self.__warning__.append(_v)

    @property
    def width(self) -> T_Element:
        return self.__width__
    @width.setter
    def width(self, _v) -> None:
        self.__width__.value= _v
    def append_width(self, _v: str|t.Iterable[str]):
        self.__width__.append(_v)

    @property
    def www_authenticate(self) -> T_Element:
        return self.__www_authenticate__
    @www_authenticate.setter
    def www_authenticate(self, _v) -> None:
        self.__www_authenticate__.value= _v
    def append_www_authenticate(self, _v: str|t.Iterable[str]):
        self.__www_authenticate__.append(_v)

    @property
    def x_content_type_options(self) -> T_Element:
        return self.__x_content_type_options__
    @x_content_type_options.setter
    def x_content_type_options(self, _v) -> None:
        self.__x_content_type_options__.value= _v
    def append_x_content_type_options(self, _v: str|t.Iterable[str]):
        self.__x_content_type_options__.append(_v)

    @property
    def x_dns_prefetch_control(self) -> T_Element:
        return self.__x_dns_prefetch_control__
    @x_dns_prefetch_control.setter
    def x_dns_prefetch_control(self, _v) -> None:
        self.__x_dns_prefetch_control__.value= _v
    def append_x_dns_prefetch_control(self, _v: str|t.Iterable[str]):
        self.__x_dns_prefetch_control__.append(_v)

    @property
    def x_forwarded_for(self) -> T_Element:
        return self.__x_forwarded_for__
    @x_forwarded_for.setter
    def x_forwarded_for(self, _v) -> None:
        self.__x_forwarded_for__.value= _v
    def append_x_forwarded_for(self, _v: str|t.Iterable[str]):
        self.__x_forwarded_for__.append(_v)

    @property
    def x_forwarded_host(self) -> T_Element:
        return self.__x_forwarded_host__
    @x_forwarded_host.setter
    def x_forwarded_host(self, _v) -> None:
        self.__x_forwarded_host__.value= _v
    def append_x_forwarded_host(self, _v: str|t.Iterable[str]):
        self.__x_forwarded_host__.append(_v)

    @property
    def x_forwarded_proto(self) -> T_Element:
        return self.__x_forwarded_proto__
    @x_forwarded_proto.setter
    def x_forwarded_proto(self, _v) -> None:
        self.__x_forwarded_proto__.value= _v
    def append_x_forwarded_proto(self, _v: str|t.Iterable[str]):
        self.__x_forwarded_proto__.append(_v)

    @property
    def x_frame_options(self) -> T_Element:
        return self.__x_frame_options__
    @x_frame_options.setter
    def x_frame_options(self, _v) -> None:
        self.__x_frame_options__.value= _v
    def append_x_frame_options(self, _v: str|t.Iterable[str]):
        self.__x_frame_options__.append(_v)

    @property
    def x_xss_protection(self) -> T_Element:
        return self.__x_xss_protection__
    @x_xss_protection.setter
    def x_xss_protection(self, _v) -> None:
        self.__x_xss_protection__.value= _v
    def append_x_xss_protection(self, _v: str|t.Iterable[str]):
        self.__x_xss_protection__.append(_v)

__all__ = ['T_Element',  "T_HTTPHeader"]

if __name__ == "__main__":
    b = T_HTTPHeader()
    b.append_set_cookie('adfhsaufhsuidhfiuashfiuahIUHUDSG*(&987132983798127398')
    b.append_set_cookie('sfsdfhuisdfhusihfuisdhfiushdfiuhsdfiu*(&987132983798127398')
    b.accept_language = 'vi-vn'
    print(b)