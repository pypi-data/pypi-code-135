from py_wechat_tools.libs.tools import dict2obj, WeChatBase


class SuperResolution(WeChatBase):

    def ai_crop(self, img_url=None, img=None):
        """
        本接口提供基于小程序的图片智能裁剪能力

        详细文档请参考：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/img/img.aiCrop.html

        :param img_url: 要检测的图片 url，传这个则不用传 img 参数
        :param img: form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。
        :return: 返回一个 WeChatData 类，包含：
                属性              类型              说明
                results         array           智能裁剪结果
                img_size        objects         图片大小

            results:    智能裁剪结果
                属性              类型              说明
                crop_left       number
                crop_top        number
                crop_right      number
                crop_bottom     number

            img_size:   图片大小
                属性              类型              说明
                w               number
                y               number
        """
        url = "https://api.weixin.qq.com/cv/img/aicrop"

        params = self.check_params(
            access_token=self.access_token,
            img_url=img_url
        )
        data = self.check_params(
            img=img
        )

        return self.post(url, params=params, data=data)

    def scan_qr_code(self, img_url=None, img=None):
        """
        本接口提供基于小程序的条码/二维码识别的API。

        详细文档请参考：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/img/img.scanQRCode.html

        :param img_url: 要检测的图片 url，传这个则不用传 img 参数
        :param img: form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。
        :return: 返回一个 WeChatData 类
                属性              类型              说明
                code_results    array           扫码结果
                img_size        objects         图片大小

            code_results:
                属性              类型              说明
                type_name       QR_CODE         类型，QR_CODE、EAN_13、CODE_128
                data            str             二维码/条形码包含的内容
                pos             WeChatDate      坐标位置，仅二维码包含该字段

            pos:
                属性              类型              说明
                left_top       WeChatDate         左上角
                right_top      WeChatDate         右上角
                right_bottom   WeChatDate         右下角
                left_bottom    WeChatDate         左下角

            left_top、right_top、right_bottom、left_bottom:
                属性              类型              说明
                x               number           x坐标
                y               number           y坐标

            img_size:   图片大小
                属性              类型              说明
                x               number           x坐标
                y               number           y坐标
        """
        url = "https://api.weixin.qq.com/cv/img/qrcode"

        params = self.check_params(
            access_token=self.access_token,
            img_url=img_url
        )
        data = self.check_params(
            img=img
        )

        return self.post(url, params=params, data=data)

    def superresolution(self, img_url=None, img=None):
        """
        本接口提供基于小程序的图片高清化能力。

        不能说效果不好，只能说几乎就是返回原图，参考本代码中的图片文件：docs/diff.png

        详细文档请参考：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/img/img.superresolution.html

        :param img_url: 要检测的图片 url，传这个则不用传 img 参数
        :param img: form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。
        :return: 返回一个 WeChatData 类，包含：
                属性              类型              说明
                media_id         string         有效期为3天，期间可以通过“获取临时素材”接口获取图片二进制
                                                .get_media() 方法获取

        """
        url = "https://api.weixin.qq.com/cv/img/superresolution"

        params = self.check_params(
            access_token=self.access_token,
            img_url=img_url,
        )
        data = self.check_params(
            img=img
        )

        return self.post(url, params=params, data=data)

    def get_media(self, media_id, file_path_name=None):
        """
        获取临时素材接口。

        该接口提供保存到本地文件，供测试使用。传入绝对路径名称，可保存到文件，如：file_path_name="/Users/mjinnn/Desktop/aaa.jpg"

        详细文档请参考：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/img/img.superresolution.html

        :param media_id: 媒体id
        :param file_path_name: 文件绝对路径和名称
        :return: , 返回图片二进制，file_path_name不为None时 返回 ok
        """
        url = "https://api.weixin.qq.com/cgi-bin/media/get"

        params = self.check_params(
            access_token=self.access_token,
            media_id=media_id,
        )
        content = self.get(url, params=params, content_type="media")
        # 保存文件
        if file_path_name:
            fo = open(file_path_name, 'wb')
            fo.write(content)
            fo.close()
            return "ok"

        return content

