#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from bs4 import BeautifulSoup

jd_Computer_html = """
<li data-sku="6805332" class="gl-item">
	<div class="gl-i-wrap">
					<div class="p-img">
						<a target="_blank" title="【1月1日爆款开门红！】爆款一口价2999！买就送专属保护壳，赠完即止，拼手速！【购iPad下单享好礼】更多惊喜猛戳" href="//item.jd.com/6805332.html" "searchlog(1,6805332,1,2,'','flagsClk=1631589000')">
							<img width="220" height="220" class="" data-img="1" source-data-lazy-img="" data-lazy-img="done" src="//img12.360buyimg.com/n7/jfs/t16759/298/1134242689/85617/2b4ccc02/5abb0fd5Nd40c72e1.jpg">
</a>						<div data-lease="" data-catid="2694" data-venid="1000000127" data-presale="" data-done="1"></div>
					</div>
					<div class="p-price">
<strong class="J_6805332" data-done="1"><em>￥</em><i>2999.00</i></strong>					</div>
					<div class="p-name p-name-type-2">
						<a target="_blank" title="【1月1日爆款开门红！】爆款一口价2999！买就送专属保护壳，赠完即止，拼手速！【购iPad下单享好礼】更多惊喜猛戳" href="//item.jd.com/6805332.html" "searchlog(1,6805332,1,1,'','flagsClk=1631589000')">
							<em>Apple iPad 平板<font class="skcolor_ljg">电脑</font> 2018年新款9.7英寸（128G WLAN版/A10 芯片/Retina显示屏/Touch ID MR7K2CH/A）银色</em>
							<i class="promo-words" id="J_AD_6805332">【1月1日爆款开门红！】爆款一口价2999！买就送专属保护壳，赠完即止，拼手速！【购iPad下单享好礼】更多惊喜猛戳</i>
						</a>
					</div>
					<div class="p-commit">
						<a target="_blank" href="//paipai.jd.com/pc/list.html?pid=6805332" class="spu-link">二手有售</a>
						<strong><a id="J_comment_6805332" target="_blank" href="//item.jd.com/6805332.html#comment" "searchlog(1,6805332,1,3,'','flagsClk=1631589000')">74万+</a>条评价</strong>
					</div>
					<div class="p-shop" data-selfware="1" data-score="5" data-reputation="99" data-done="1">
<span class="J_im_icon"><a target="_blank" class="curr-shop" "searchlog(1,1000000127,0,58)" href="//mall.jd.com/index-1000000127.html" title="京东Apple产品专营店">京东Apple产品专营店</a><b class="im-02" style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;" title="联系客服" "searchlog(1,1000000127,0,61)"></b></span>					</div>
					<div class="p-icons" id="J_pro_6805332" data-done="1">
			<i class="goods-icons J-picon-tips J-picon-fix" data-idx="1" data-tips="京东自营，品质保障">自营</i>
						<i class="goods-icons4 J-picon-tips J-picon-fix" data-tips="天天低价，正品保证">秒杀</i><i class="goods-icons4 J-picon-tips" data-tips="购买本商品送赠品">赠</i>
<i class="goods-icons4 J-picon-tips" data-tips="购买本商品送赠品">赠</i>					</div>
					<div class="p-operate">
						<a class="p-o-btn contrast J_contrast" data-sku="6805332" href="javascript:;" "searchlog(1,6805332,1,6,'','flagsClk=1631589000')"><i></i>对比</a>
						<a class="p-o-btn focus J_focus" data-sku="6805332" href="javascript:;" "searchlog(1,6805332,1,5,'','flagsClk=1631589000')"><i></i>关注</a>
						<a class="p-o-btn addcart" href="//cart.jd.com/gate.action?pid=6805332&amp;pcount=1&amp;ptype=1" target="_blank" "searchlog(1,6805332,1,4,'','flagsClk=1631589000')" data-limit="0"><i></i>加入购物车</a>
					</div>
	</div>
</li>
"""

soup = BeautifulSoup(jd_Computer_html, "lxml")

Computer_price = soup.find('div', attrs={'class':'p-price'}).find('i').text
print(f"电脑的价格为：{Computer_price}元")

Computer_name = soup.find('div', attrs={'class':'p-name p-name-type-2'}).find('em').text
print(f"电脑的名称为：{Computer_name}")

#电脑的价格为：2999.00元
#电脑的名称为：Apple iPad 平板电脑 2018年新款9.7英寸（128G WLAN版/A10 芯片/Retina显示屏/Touch ID MR7K2CH/A）银色
