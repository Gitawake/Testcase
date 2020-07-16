# -*- coding: utf-8 -*-
import time

from bin.StartStopControl import BaseTestCase


class Qzz(BaseTestCase):
    def start_up(self):
        # 启动app
        self.d.session("com.zsyj.videomake")
        if self.d(resourceId="com.zsyj.videomake:id/btn_dialog_open").exists:  # 首次启动
            self.d(resourceId="com.zsyj.videomake:id/btn_dialog_open").click()
            self.d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click()
            time.sleep(1)
            self.d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click()
        elif self.d(text="是否允许“趣制作”获取此设备的位置信息？").exists:
            self.d(resourceId="com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
        # 如果有开屏广告就点击跳过
        if self.d(resourceId="com.zsyj.videomake:id/tt_splash_skip_btn").wait(timeout=3.0):
            self.d(resourceId="com.zsyj.videomake:id/tt_splash_skip_btn").click()
        # 如果有更新弹窗就触发返回按钮取消弹窗
        if self.d(resourceId="com.zsyj.videomake:id/tv_update").exists:
            self.d.press("back")

    def test_qzz_top_vip_1nvx(self):
        Qzz.start_up(self)
        self.d(resourceId="com.zsyj.videomake:id/iv_open_vip").click()
        self.d(resourceId="com.zsyj.videomake:id/tv_pay").click()
        if self.d(resourceId="com.zsyj.videomake:id/layout_we_chat_login").exists:
            self.d(resourceId="com.zsyj.videomake:id/layout_we_chat_login").click()
            self.d(resourceId="com.zsyj.videomake:id/tv_pay").wait(5.0)
            self.d(resourceId="com.zsyj.videomake:id/tv_pay").click()
        self.d(text='支付').wait(5.0)
        assert self.d(text='支付').exists

    def test_qzz_top_vip_1yzfb(self):
        Qzz.start_up(self)
        self.d(resourceId="com.zsyj.videomake:id/iv_open_vip").click()
        self.d(resourceId="com.zsyj.videomake:id/rl_price1").click()
        self.d(resourceId="com.zsyj.videomake:id/img_zfb_select").click()
        self.d(resourceId="com.zsyj.videomake:id/tv_pay").click()
        if self.d(resourceId="com.zsyj.videomake:id/layout_we_chat_login").exists:
            self.d(resourceId="com.zsyj.videomake:id/layout_we_chat_login").click()
            self.d(resourceId="com.zsyj.videomake:id/tv_pay").wait(5.0)
            self.d(resourceId="com.zsyj.videomake:id/tv_pay").click()
        self.d(text='点击下方头像登录').wait(5.0)
        assert self.d(text='点击下方头像登录').exists

    def test_qzz_top_search(self):
        Qzz.start_up(self)
        self.d(resourceId="com.zsyj.videomake:id/search_img").click()
        self.d(resourceId="com.zsyj.videomake:id/cv_et_search").send_keys(text="飞天")
        self.d(resourceId="com.zsyj.videomake:id/tv_search").click()
        self.d.xpath(
            '//*[@resource-id="com.zsyj.videomake:id/recycler_view_search_video"]/android.widget.LinearLayout[1]').click()
        assert self.d(resourceId='com.zsyj.videomake:id/cycle').exists

    def test_qzz_top_tool_course_more(self):
        Qzz.start_up(self)
        self.d(resourceId="com.zsyj.videomake:id/iv_video_tool").click()
        self.d(text="更多").click()
        self.d.xpath('//*[@resource-id="com.zsyj.videomake:id/rv_course"]/android.widget.LinearLayout[1]').click()
        assert self.d(resourceId='com.zsyj.videomake:id/seekBarCourse').exists

    def test_qzz_top_tool_course(self):
        Qzz.start_up(self)
        self.d(resourceId="com.zsyj.videomake:id/iv_video_tool").click()
        self.d.xpath(
            '//*[@resource-id="com.zsyj.videomake:id/rv_video_tool_course"]/android.widget.FrameLayout[2]/android.widget.ImageView[1]').click()
        assert self.d(resourceId='com.zsyj.videomake:id/seekBarCourse').exists

    def test_qzz_top_tool_canvas_scale(self):
        Qzz.start_up(self)
        self.d(resourceId="com.zsyj.videomake:id/iv_video_tool").click()
        self.d(resourceId="com.zsyj.videomake:id/cv_ll_tool_crop_one").click()
        self.d.xpath(
            '//*[@resource-id="com.zsyj.videomake:id/cv_crop_video_grid"]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
        self.d(resourceId="com.zsyj.videomake:id/rb_169").click()
        self.d(resourceId="com.zsyj.videomake:id/tv_bjys").click()
        self.d(resourceId="com.zsyj.videomake:id/tv_bg_blur").click()
        self.d.xpath('//*[@resource-id="com.zsyj.videomake:id/rlv_bg_color"]/android.widget.RelativeLayout[5]').click()
        self.d(resourceId="com.zsyj.videomake:id/tv_bg_local").click()
        self.d.xpath('//*[@resource-id="com.zsyj.videomake:id/recycler"]/android.widget.FrameLayout[1]').click()
        self.d(resourceId="com.zsyj.videomake:id/btn_ok").click()
        self.d(resourceId="com.zsyj.videomake:id/tv_next").click()
        self.d(resourceId="com.zsyj.videomake:id/mVideoPlayer").wait(10.0)
        assert self.d(resourceId='com.zsyj.videomake:id/mVideoPlayer').exists

    def test_qzz_top_tool_length_cutting(self):
        Qzz.start_up(self)
        self.d(resourceId="com.zsyj.videomake:id/iv_video_tool").click()
        self.d(resourceId="com.zsyj.videomake:id/cv_ll_tool_cut_time").click()
        self.d.xpath(
            '//*[@resource-id="com.zsyj.videomake:id/cv_crop_video_grid"]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
        time.sleep(1)
        self.d.swipe(157, 2203, 339, 2203)
        self.d(resourceId="com.zsyj.videomake:id/tv_next").click()
        self.d(resourceId="com.zsyj.videomake:id/mVideoPlayer").wait(10.0)
        assert self.d(resourceId='com.zsyj.videomake:id/mVideoPlayer').exists
