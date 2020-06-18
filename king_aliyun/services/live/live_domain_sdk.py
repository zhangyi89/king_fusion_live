"""
直播模块: 域名管理
"""

import json

from aliyunsdklive.request.v20161101.AddLiveDomainRequest import AddLiveDomainRequest
from aliyunsdklive.request.v20161101.AddLiveDomainMappingRequest import AddLiveDomainMappingRequest
from aliyunsdklive.request.v20161101.DeleteLiveDomainRequest import DeleteLiveDomainRequest
from aliyunsdklive.request.v20161101.DeleteLiveDomainMappingRequest import DeleteLiveDomainMappingRequest
from aliyunsdklive.request.v20161101.BatchDeleteLiveDomainConfigsRequest import BatchDeleteLiveDomainConfigsRequest
from aliyunsdklive.request.v20161101.BatchSetLiveDomainConfigsRequest import BatchSetLiveDomainConfigsRequest
from aliyunsdklive.request.v20161101.StartLiveDomainRequest import StartLiveDomainRequest
from aliyunsdklive.request.v20161101.StopLiveDomainRequest import StopLiveDomainRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainBpsDataRequest import DescribeLiveDomainBpsDataRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainBpsDataByTimeStampRequest import \
    DescribeLiveDomainBpsDataByTimeStampRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainConfigsRequest import DescribeLiveDomainConfigsRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainDetailRequest import DescribeLiveDomainDetailRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainFrameRateAndBitRateDataRequest import \
    DescribeLiveDomainFrameRateAndBitRateDataRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainLimitRequest import DescribeLiveDomainLimitRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainMappingRequest import DescribeLiveDomainMappingRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainOnlineUserNumRequest import \
    DescribeLiveDomainOnlineUserNumRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainPushBpsDataRequest import \
    DescribeLiveDomainPushBpsDataRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainPushTrafficDataRequest import \
    DescribeLiveDomainPushTrafficDataRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainRealTimeBpsDataRequest import \
    DescribeLiveDomainRealTimeBpsDataRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainRealTimeHttpCodeDataRequest import \
    DescribeLiveDomainRealTimeHttpCodeDataRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainRealTimeTrafficDataRequest import \
    DescribeLiveDomainRealTimeTrafficDataRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainRealtimeLogDeliveryRequest import \
    DescribeLiveDomainRealtimeLogDeliveryRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainRecordDataRequest import \
    DescribeLiveDomainRecordDataRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainSnapshotDataRequest import \
    DescribeLiveDomainSnapshotDataRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainTrafficDataRequest import \
    DescribeLiveDomainTrafficDataRequest
from aliyunsdklive.request.v20161101.DescribeLiveDomainTranscodeDataRequest import \
    DescribeLiveDomainTranscodeDataRequest
from aliyunsdklive.request.v20161101.DescribeLiveTopDomainsByFlowRequest import \
    DescribeLiveTopDomainsByFlowRequest
from aliyunsdklive.request.v20161101.DescribeLiveUserDomainsRequest import DescribeLiveUserDomainsRequest
from aliyunsdklive.request.v20161101.ListLiveRealtimeLogDeliveryDomainsRequest import \
    ListLiveRealtimeLogDeliveryDomainsRequest
from aliyunsdklive.request.v20161101.ModifyLiveDomainSchdmByPropertyRequest import \
    ModifyLiveDomainSchdmByPropertyRequest
from aliyunsdklive.request.v20161101.SetLiveDomainCertificateRequest import SetLiveDomainCertificateRequest
from aliyunsdklive.request.v20161101.UpdateLiveTopLevelDomainRequest import UpdateLiveTopLevelDomainRequest

from king_aliyun.services.common import client


class LiveDomainSDK:

    def __init__(self):
        self.client = client

    def add_live_domain(self, domain_name: str, region: str, live_domain_type: str, scope: str) -> object:
        """添加直播域名，一次只能提交一个域名
        限制条件：
            创建直播域名之前，必须先开通阿里云live服务。
            直播域名必须已备案完成。

        :param domain_name: 需要添加的直播域名，支持泛域名，以符号“.”开头，如：.a.com。
        :param region: 直播域名单元化信息 (cn-shenzhen：华南1, cn-beijing：华北2)，具体取值查看阿里云支持区域
        :param live_domain_type: 直播域名类型 (liveEdge： 边缘推流域名, liveVideo: 播流域名 )
        :param scope: 直播加速区域 (global： 全球加速, domestic：国内, overseas：海外)
        :return: {"code":"DomainNotRegistration","message":"该域名没有备案，请先备案。"}
        :rtype: object
        """
        request = AddLiveDomainRequest()

        request.set_DomainName(domain_name)
        request.set_LiveDomainType(live_domain_type)
        request.set_Region(region)
        request.set_Scope(scope)
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

        response = json.loads(self.client.do_action_with_exception(request))
        return response

    def delete_live_domain(self, domain_name: str) -> object:
        """删除已添加的直播域名
        删除本条直播域名的全部相关记录

        :param domain_name: 需要删除的直播域名
        :return: {"code":"InvalidDomain.NotFound","message":"当前账户下未查到域名，请您确认该域名是否正确。"}
        :rtype: object
        """
        request = DeleteLiveDomainRequest()

        request.set_DomainName(domain_name)
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

        response = json.loads(self.client.do_action_with_exception(request))
        return response

    def add_live_domain_mapping(self, pull_domain: str, push_domain: str) -> object:
        """添加直播域名播流域名和推流域名的映射关系配置
        :param pull_domain: 播流域名，域名类型为liveVideo
        :param push_domain: 推流域名，域名类型为liveEdge
        :return: {"code":"InvalidDomain.NotFound","message":"当前账户下未查到域名，请您确认该域名是否正确。"}
        :rtype: object
        """
        request = AddLiveDomainMappingRequest()

        request.set_PullDomain(pull_domain)
        request.set_PushDomain(push_domain)
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

        response = json.loads(self.client.do_action_with_exception(request))
        return response

    def delete_live_domain_mapping(self, pull_domain: str, push_domain: str) -> object:
        """删除直播域名播流域名和推流域名的映射关系配置
        :param pull_domain: 播流域名，域名类型为liveVideo
        :param push_domain: 推流域名，域名类型为liveEdge
        :return: {"code":"InvalidDomain.NotFound","message":"当前账户下未查到域名，请您确认该域名是否正确。"}
        :rtype: object
        """
        request = DeleteLiveDomainMappingRequest()

        request.set_PullDomain(pull_domain)
        request.set_PushDomain(push_domain)
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

        response = json.loads(self.client.do_action_with_exception(request))
        return response

    def start_live_domain(self, domain_name: str) -> object:
        """启用状态为停用的直播域名，将DomainStatus变更为online
        说明: 域名对应账户如果欠费，或域名处于非法状态，无法正常调用该接口启用直播域名
        :param domain_name: 需要启动的直播域名
        :return: {"code":"InvalidDomain.NotFound","message":"当前账户下未查到域名，请您确认该域名是否正确。"}
        :rtype: object
        """
        request = StartLiveDomainRequest()

        request.set_DomainName(domain_name)
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

        response = json.loads(self.client.do_action_with_exception(request))
        return response

    def stop_live_domain(self, domain_name: str) -> object:
        """停用某个直播域名，将DomainStatus变更为offline
        说明: 停用该直播域名后，该条直播域名信息仍保留，针对直播域名的请求，系统将自动回源处理。
        :param domain_name: 需要停用的直播域名
        :return: {"code":"InvalidDomain.NotFound","message":"当前账户下未查到域名，请您确认该域名是否正确。"}
        :rtype: object
        """
        request = StopLiveDomainRequest()

        request.set_DomainName(domain_name)
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

        response = json.loads(self.client.do_action_with_exception(request))
        return response

    def batch_set_live_domain_configs(self, domain_names: str, functions: str) -> object:
        """批量配置域名
        :param domain_names: 直播域名，多个用英文半角逗号分隔
        :param functions: 功能列表
                [{"functionArgs":[{"argName":"domain_name","argValue":"home.1sapp.com"}],"functionName":"set_req_host_header"}]
        :return: {"code":"InvalidDomain.NotFound","message":"当前账户下未查到域名，请您确认该域名是否正确。"}
        :rtype: object
        """
        request = BatchSetLiveDomainConfigsRequest()

        request.set_DomainNames(domain_names)
        request.set_Functions(functions)
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

        response = json.loads(self.client.do_action_with_exception(request))
        return response

    def batch_delete_live_domain_configs(self, domain_names: str, function_names: str) -> object:
        """批量删除域名配置
        :param domain_names: 加速域名，多个用英文半角逗号分隔。
        :param function_names: 功能列表名称，用逗号分隔。
        :return: {"code":"InvalidDomain.NotFound","message":"当前账户下未查到域名，请您确认该域名是否正确。"}
        :rtype: object
        """
        request = BatchDeleteLiveDomainConfigsRequest()

        request.set_DomainNames(domain_names)
        request.set_FunctionNames(function_names)
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

        response = json.loads(self.client.do_action_with_exception(request))
        return response

    def describe_live_domain_bps_data(self):
        """查询直播域名的网络带宽监控数据
        1. 不指定StartTime和EndTime时，默认读取过去24小时的数据，同时支持按指定的起止时间查询，两者需要同时指定。
        2. 支持批量域名查询，多个域名用逗号（半角）分隔。
        3. 最多可获取最近90天的数据。
        """
        request = DescribeLiveDomainBpsDataRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_bps_data_by_timestamp(self):
        request = DescribeLiveDomainBpsDataByTimeStampRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_configs(self):
        """查询直播域名配置，一次可查询多个功能配置"""
        request = DescribeLiveDomainConfigsRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_detail(self):
        """获取指定直播域名配置的基本信息"""
        request = DescribeLiveDomainDetailRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        # python2:  print(response)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_frame_rate_and_bit_rate_data(self):
        """调用查询直播域名下流帧率和码率数据。
        说明: 数据采集和统计有一定延迟，建议查询5分钟前的数据。
        """
        request = DescribeLiveDomainFrameRateAndBitRateDataRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_limit(self):
        request = DescribeLiveDomainLimitRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_mapping(self):
        request = DescribeLiveDomainMappingRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_online_user_num(self):
        """调用DescribeLiveDomainOnlineUserNum查询域名下所有流某分钟的在线人数信息
        说明: 本接口只支持flv和rtmp播放在线人数统计，暂不支持hls播放在线人数统计
        说明: 数据采集和统计有一定延迟，建议查询5分钟前的数据
        """
        request = DescribeLiveDomainOnlineUserNumRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_push_bps_data(self):
        request = DescribeLiveDomainPushBpsDataRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_push_traffic_data(self):
        request = DescribeLiveDomainPushTrafficDataRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_real_time_bps_data(self):
        """调用DescribeLiveDomainRealTimeBpsData获取域名1分钟粒度带宽数据
           - 可以查询7天内的数据，单次查询StartTime和EndTime跨度不能超过24小时
           - 如果StartTime和EndTime均未指定，默认返回当前时间起一小时内的数据
        """
        request = DescribeLiveDomainRealTimeBpsDataRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_real_time_http_code_data(self):
        """获取加速域名1分钟粒度的HTTP返回码占比数据。
           - 单次查询StartTime和EndTime跨度不能超过24小时。
           - 如果StartTime和EndTime均未指定, 默认返回当前时间起一小时内的数据。
           - 支持批量域名查询，多个域名用逗号（半角）分隔。
           - 最多可获取最近7天的数据。
        """
        request = DescribeLiveDomainRealTimeHttpCodeDataRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_real_time_traffic_data(self):
        """获取加速域名的1分钟流量监控数据。
            - 不指定StartTime和EndTime时，默认读取过去 1 小时的数据，同时支持按指定的起止时间查询，两者需要同时指定。
            - 支持批量域名查询，多个域名可用逗号（半角）分隔。
            - 最多可获取最近90天的数据。
        """
        request = DescribeLiveDomainRealTimeTrafficDataRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_real_time_log_delivery(self):
        request = DescribeLiveDomainRealtimeLogDeliveryRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_record_data(self):
        """查询直播域名录制时长数据。
            - 支持用户查询单个直播域名在指定时间区段内的每日录制时长数据。
            - 每日录制时长数据包括：当日录制总时长和区分录制格式的时长数据列表。
            - 支持查询2018/01/01起的数据，数据查询的起止时间跨度最大为90天。
        """
        request = DescribeLiveDomainRecordDataRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_snapshot_data(self):
        """调用查询直播域名截图张数数据。
            - 支持用户查询单个直播域名在指定时间区段内的每日截图张数。
            - 支持查询2018/01/01起的数据，数据查询的起止时间跨度最大为90天。
        """
        request = DescribeLiveDomainSnapshotDataRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_traffic_data(self):
        """查询直播域名网络流量监控数据。
            - 不指定StartTime和EndTime时，默认读取过去24小时的数据，同时支持按指定的起止时间查询，两者需要同时指定。
            - 支持批量域名查询，多个域名用逗号（半角）分隔。
            - 最多可获取最近90天的数据。
        """
        request = DescribeLiveDomainTrafficDataRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_domain_trans_code_data(self):
        """查询直播域名转码时长数据。
            - 支持用户查询单个直播域名在指定时间区段内的每日转码时长数据。
            - 每日转码时长数据包括：当日转码总时长和区分转码规格的时长数据列表。
            - 支持查询2018/01/01起的数据，数据查询的起止时间跨度最大为90天。
        """
        request = DescribeLiveDomainTranscodeDataRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_top_domains_by_flow(self):
        request = DescribeLiveTopDomainsByFlowRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def describe_live_user_domains(self):
        """查询用户名下所有的直播域名。
            - 支持域名模糊匹配过滤、域名所处region过滤。
        """
        request = DescribeLiveUserDomainsRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def list_live_real_time_log_delivery_domains(self):
        request = ListLiveRealtimeLogDeliveryDomainsRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def modify_live_domain_schdm_by_property(self):
        request = ModifyLiveDomainSchdmByPropertyRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def set_live_domain_certificate(self):
        """调用设置某域名下证书功能是否启用及修改证书信息。"""
        request = SetLiveDomainCertificateRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))

    def update_live_top_level_domain(self):
        request = UpdateLiveTopLevelDomainRequest()
        request.set_accept_format('json')

        response = self.client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))
