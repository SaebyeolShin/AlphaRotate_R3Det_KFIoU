# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

sys.path.append("../../")

from alpharotate.libs.models.detectors.r3det_kfiou import build_whole_network
from tools.test_dota_base_sota import TestDOTA
from configs import cfgs


class TestDOTAR3DetKF(TestDOTA):

    def eval(self):
        txt_name = '{}.txt'.format(self.cfgs.VERSION)
        real_test_img_list = self.get_test_image()

        r3det_kf = build_whole_network.DetectionNetworkR3DetKF(cfgs=self.cfgs,
                                                               is_training=False)
                                                               
        self.test_dota(det_net=r3det_kf, real_test_img_list=real_test_img_list, txt_name=txt_name)

        if not self.args.show_box:
            os.remove(txt_name)

if __name__ == '__main__':

    tester = TestDOTAR3DetKF(cfgs)
    tester.eval()


