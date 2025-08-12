from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("xiaobaoyun", "筱富瑞", "一个简单的菜单插件", "1.0.0")
class XiaoBaoYunPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("菜单")
    async def show_menu(self, event: AstrMessageEvent):
        """显示菜单内容"""
        menu_content = """
        A.C助手
        -----
        抢包功能 抢包设置 群发功能
        群管功能 点歌功能 个人助手
        问答功能 发包功能 头衔功能
        捡漏功能 定时功能 循环任务
        续火功能 打卡功能 艾特处理
        戳人功能 防撤功能 监控功能
        召唤功能 伪造聊天 名片功能
        收款功能 备注功能 互赞功能
        娱乐功能 清屏功能 自身撤回
        秒赞功能 触发模式 静默模式
        自动处理 菜单配置 测挂功能
        自助上管 文件监控 提示功能
        拉黑功能 基础群管 入群验证
        其他功能 字符功能 水印功能
        被戳处理 敬请期待 敬请期待
        """
        yield event.plain_result(menu_content)

    async def terminate(self):
        """插件卸载或停用时的清理工作"""
        pass
