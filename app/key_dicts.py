row_keys = {
    "china_bank": {"客户号", "日期", "付款人账号", "收款人账号", "付款人名称", "收款人名称", "付款人开户行", "收款人开户行", "金额", "业务种类", "业务编号", "凭证字号",
                   "纳税人识别号", "缴款书交易流水号", "税票号码", "纳税人全称", "征收机关名称", "收款国库（银行）名称", "交易机构", "交易渠道", "交易流水号", "经办", "回单编号",
                   "回单验证码", "打印时间", "打印次数", "报文种类", "业务类型", "业务识别号", "发起行行号", "发起行名称", "入账账号", "用途", "附言", "收支申报号",
                   "业务编号", "接收行行号", "接收行名称", "入账户名", "凭证号码", "备注", "起息日", "到期日", "存期", "册号", "序号", "利率", "扣账账号",
                   "扣账户名"},
    "construction_bank": {"币别", "流水号：", "全称", "账号", "开户行", "[(]大写[)]", "[(]小写[)]", "凭证种类", "凭证号码", "结算方式", "用途", "打印柜员",
                          "打印机构", "打印卡号", "生成时间", "交易柜员", "交易机构", "汇款交易日期", "汇款合约编号", "实际收款人账户", "实际收款人户名", "实际收款人汇入行",
                          "汇出行行名", "汇款备注", "汇款附言", "支付清算业务类型", "付款方式", "转账日期", "纳税人全称及纳税人识别号", "合计金额"},
    "communications_bank": {"回单编号", "回单类型", "业务名称", "凭证种类", "凭证号码", "借贷标志", "转账方式", "付款人账号", "付款人名称", "开户行名称", "收款人账号",
                            "收款人名称", "币种", "金额", "金额大写", "摘要", "附加信息", "打印次数", "记账日期", "会计流水号", "打印机构", "打印柜员", "记账机构",
                            "经办柜员", "记账柜员", "复核柜员", "授权柜员", "批次号", "总张数", "当前第", "人民币"},
    "agricultural_bank": {"交易日期", "日期", "序号", "校验码", "户名", "账号", "开户行", "金额", "[(]人民币[)]", "摘要", "附言",
                          "内部成员单位账号", "交易时间", "打印日期"},
    "minsheng_bank": {"交易日期", "交易流水号", "付款人账号", "收款人账号", "付款人名称", "收款人名称", "付款人开户行", "收款人开户行", "币种", "金额", "[(]大写[)]",
                      "[(]小写[)]", "银行附言", "客户附言", "记账流水号", "提示", "登录号", "网点编号", "打印状态", "客户验证码", "柜员号", "打印方式", "打印日期",
                      "电子凭证号", "记账流水号", "交易类型", "通道", "业务种类", "实际记账账号", "页码", "业务类型", "账号", "户名", "开户行"},
    "hz_bank": {"户名", "账号", "交易币种", "金额[(]小写[)]", "金额[(]大写[)]", "手续费[(]小写[)]", "手续费[(]大写[)]", "交易时间", "摘要", "对方机构名称",
                "附言", "打印时间"},
    "jiangnan_rural_commercial_bank": {"交易日期", "交易渠道", "回单名称", "记账日期", "发起清算行行号", "发起行行号", "付款人账号", "付款人名称", "付款人开户行行号",
                                       "币种", "金额[(]大写[)]", "附言", "核心流水号", "委托日期", "业务种类", "支付交易序号", "接收行行号", "收款人账号",
                                       "收款人名称", "收款人开户行行号", "金额[(]小写[)]", "打印日期", "打印机构", "打印渠道", "打印设备编号", "备注",
                                       "付款人开户行", "流水号", "手续费", "工本费", "邮电费", "发起行名称", "转账日期", "凭证号", "纳税人编码", "纳税人名称",
                                       "收款国库名称", "征收机关名称", "税种", "利息金额[(]大写[)]", "利息金额[(]小写[)]", "利率[(]%[)]", "用途",
                                       "回单种类"},
    "nt_bank": {"打印日期", "流水号", "交易时间", "账号", "户名", "开户行", "币种", "金额", "小写", "合计", "手续费", "合计[(]大写[)]", "用途",
                "银行[(]盖章[)]", "备注", "转账"},
    "nanjing_bank": {"电子回单号", "交易流水号", "户名", "帐号", "开户银行", "金额[（]大写[）]", "交易金额", "交易日期", "时间戳", "凭证号",
                     "交易名称", "备注信息", "电子回单验证码", "摘要内容", "本回单打印次数", "打印日期", "注意"},
    "ningbo_bank": {"交易日期", "回单编号", "^账号", "^户名", "开户银行", "人民币", "RMB", "回单种类", "交易渠道", "业务种类", "打印方式", "打印时间", "交易网点",
                    "操作员", "交易流水", "交易金额", "备注", "[\u4e00-\u9fa5]{1,}\d{8}[-]\d{8}", "付款人账号", "付款人户名"},
    "xian_bank": {"付款户名", "付款账号", "付款行名", "金额[(]大写[)]", "金额[(]小写[)]", "人民币", "收款户名", "收款账号", "收款行名",
                  "[壹贰叁肆伍陆柒捌玖拾佰仟万亿元圆角分零整正]{2,}"},
    "industrial_and_commercial_bank": {"户名", "账号", "开户银行", "金额", "金额[(]大写[)]", "摘要", "用途", "业务[(]产品[)]种类", "交易流水号",
                                       "时间戳", "记账网点", "记账柜员", "记账日期", "人民币"},
    "citic_bank": {"名称", "账号", "开户行名", "开户行号", "币种及金额", "RMB", "付方资金分簿编号", "收方资金分簿编号", "付方资金分簿名称", "收方资金分簿名称"},
    "zijin_rural_commercial_bank": {"回单类型", "付款人账号", "收款人账号", "付款行行号", "收款行行号", "回单号", "付款人户名", "收款人户名", "付款行行名",
                                    "收款行行名", "交易日期", "凭证号", "用途", "金额[(]大写[)]", "金额[(]小写[)]", "打印次数", "开户机构", "流水号",
                                    "币种", "打印时间", "支付序号", "前置流水号", "交易金额[(]大写[)]", "交易金额[(]小写[)]"}
}

column_keys = {
    "china_bank": {("税（费）种名称", 8, "[\u4e00-\u9fa5]{1,}"), ("所属日期", 9, "\d{4,}[/]\d{2}[/]\d{2}"),
                   ("实缴金额", 8, "\d{1,}[.]\d{2}"), ("手机号个数", 8, "\d"), ("收费类型", 8, "[\u4e00-\u9fa5]{1,}"),
                   ("费用账期", 8, "\d{4,}"), ("金额", 9, "\d{1,}"), },
    "construction_bank": {("项目名称", 8, "[\u4e00-\u9fa5]{1,}"), ("工本费/转账汇款手续费/手续费", 8, "^\d{1,}.\d{2}$"),
                          ("金额", 9, "^\d{1,}.\d{2}$"), ("税（费）种名称", (7, 8), "^[\u4e00-\u9fa5]{1,}$"),
                          ("所属时期", (7, 8), "\d{8}"), ("实缴金额", 7, "\d{1,}[.]\d{2}"), ("计息项目", 8, "[\u4e00-\u9fa5]{1,}"),
                          ("起息日", 8, "\d{8}"), ("结息日", 8, "\d{8}"), ("本金/积数", (8, 9), "^\d{1,}[.]\d{1,2}$"),
                          ("利率(%)", (8, 9), "^\d{1,}[.]\d{1,}$"), ("利息", (8, 9), "^￥[0-9,]{1,}[.]\d{2}$"),
                          ("工本费/转账汇款手续费/手续费金额", (7, 8, 9), "^\d{1,}.\d{2}$")},
    "communications_bank": {},
    "agricultural_bank": {},
    "minsheng_bank": {("税（费）种名称", 8, "[\u4e00-\u9fa5]{1,}"), ("税款所属时期", (8, 9), "[-]?\d{8}"),
                      ("实缴金额", (7, 8), "\d{1,}[.]\d{2}"), ("起息日", 8, "\d{4}[-]\d{2}[-]\d{2}"),
                      ("结息日", 8, "\d{4}[-]\d{2}[-]\d{2}"), ("计息天数", 8, "\d{1,4}"),
                      ("利率(%)", (7, 8), "^\d{1}[.]\d{1}$"), ("本金/积数", 8, "^\d{1,}[.]\d{2}$"),
                      ("利息", (7, 8), "^\d{1,}[.]\d{3,}$")},
    "hz_bank": {},
    "jiangnan_rural_commercial_bank": {},
    "nt_bank": {},
    "nanjing_bank": {},
    "ningbo_bank": {},
    "xian_bank": {},
    "industrial_and_commercial_bank": {},
    "citic_bank": {},
    "zijin_rural_commercial_bank": {}
}

multiple_lines_info = {
    "china_bank": {"付款人名称": (6, 8), "收款人名称": (6, 8), "付款人开户行": 8, "收款人开户行": 8, "发起行名称": 8, "接收行名称": 8, "业务编号": 6,
                   "附言": 6},
    "construction_bank": {"纳税人全称及纳税人识别号": (6, 9), "用途": (6, 9), "付款人开户行": (6, 9), "收款人开户行": (6, 9)},
    "communications_bank": {"附加信息": (6, 9)},
    "agricultural_bank": {"金额": 9},
    "minsheng_bank": {"付款人开户行": (3, 9), "收款人开户行": (3, 9), "付款人开户银行": (3, 6, 9), "银行附言": "6+", "客户附言": "6+", "摘要": "6+"},
    "hz_bank": {},
    "jiangnan_rural_commercial_bank": {"利息金额(小写)": 6},
    "nt_bank": {},
    "nanjing_bank": {"户名": (3, 6, 9)},
    "ningbo_bank": {"收款行行名": "line_break", "收款人名称": "line_break", "付款行行名": "line_break", "付款人名称": "line_break"},
    "xian_bank": {"付款户名": (6, 9), "收款行名": (6, 8), "收款户名": (6, 9), "付款行名": (6, 8), "金额(小写)": 6, "金额(大写)": 6},
    "industrial_and_commercial_bank": {"开户银行": (3, 9)},
    "citic_bank": {},
    "zijin_rural_commercial_bank": {}
}

duplicate_keys = {
    "construction_bank": (("全称", "账号", "开户行"), "付款人", "收款人"),
    "communications_bank": (("开户行名称"), "付款人", "收款人"),
    "agricultural_bank": (("账号", "户名", "开户行"), "付款人", "收款人"),
    "hz_bank": (("账号", "户名"), "付款人", "收款人"),
    "nt_bank": (("账号", "户名", "开户行"), "付款人", "收款人"),
    "nanjing_bank": (("户名", "帐号", "开户银行"), "客户信息", "对方信息"),
    "industrial_and_commercial_bank": (("户名", "账号", "开户银行"), "付款人", "收款人"),
    "citic_bank": (("名称", "账号", "开户行名", "开户行号"), "付款人", "收款人")
}

splits = {
    "china_bank": {"国内支付业务收款回单", "国内支付业务付款回单", "客户借记回单", "客户付费回单", "利息收入回单"},
    "construction_bank": {"中国建设银行单位客户专用回单"},
    "communications_bank": {"^回$"},
    "agricultural_bank": {"中国农业银行江苏分行电子回单", "中国农业银行苏州分行电子回单"},
    "minsheng_bank": {"支付业务回单", "电子银行业务回单", "电子缴税付款凭证", "存款利息回单", "客户通用记账凭证", "网上代发工资回单", "深圳金融结算系统回单", "社保基金电子交款回单"},
    "hz_bank": {"杭州银行电子回单"},
    "jiangnan_rural_commercial_bank": {"^客$"},
    "nt_bank": {"电子银行交易明细"},
    "nanjing_bank": {"南京银行网上银行电子回单"},
    "ningbo_bank": {"宁波银行客户回单"},
    "xian_bank": {"收费凭证", "汇兑来账凭证", "转账凭证", "现金支取凭证", "存款利息凭证", "汇兑往账凭证"},
    "industrial_and_commercial_bank": {"中国工商银行"},
    "citic_bank": {"客户回单"},
    "zijin_rural_commercial_bank": {"紫金农商银行回单"}
}

common = {"date": r"\d{4}[年]\d{2}[月]\d{2}[日]",
          "id": r"NO[.]\d{0,}",
          "describe": r"此回单以客户真实交易为依据|如您已通过银行网点取得相应纸质回单|普通汇款业务不保证实时到账|本行所提供客户网上自助打印回单不作为任何债权债务凭据|次打印|电子回单验证处进行回单验证|将此电子回单发送给指定的接收人",
          "time": r"\d{2}:\d{2}:\d{2}",
          "title": r"国内支付业务收款回单|国内支付业务付款回单|客户借记回单|客户付费回单|利息收入回单|中国建设银行单位客户专用回单|回单|中国农业银行江苏分行电子回单|中国农业银行苏州分行电子回单|支付业务回单|电子银行业务回单|电子缴税付款凭证|杭州银行电子回单|电子银行交易明细|存款利息回单|客户通用记账凭证|网上代发工资回单|深圳金融结算系统回单|社保基金电子交款回单|南京银行网上银行电子回单|宁波银行客户回单|收费凭证|汇兑来账凭证|转账凭证|现金支取凭证|存款利息凭证|汇兑往账凭证|中国工商银行|网上银行电子回单|客户回单|紫金农商银行回单",
          "money": "[￥]\d{1,}.\d{2}",
          "money_chinese": r"[壹贰叁肆伍陆柒捌玖拾佰仟万亿元圆角分零整正]{2,}"}

y_concat_threshold = {"china_bank": 10, "construction_bank": 10, "communications_bank": 10, "agricultural_bank": 10,
                      "minsheng_bank": 10, "hz_bank": 10, "jiangnan_rural_commercial_bank": 6, "nt_bank": 10,
                      "nanjing_bank": 8, "ningbo_bank": 10, "xian_bank": 10, "industrial_and_commercial_bank": 10,
                      "citic_bank": 10, "zijin_rural_commercial_bank": 10}

right_threshold = {"china_bank": 40, "construction_bank": 40, "communications_bank": 40, "agricultural_bank": 80,
                   "minsheng_bank": 70, "hz_bank": 180, "jiangnan_rural_commercial_bank": 40, "nt_bank": 40,
                   "nanjing_bank": 120, "ningbo_bank": 60, "xian_bank": 40, "industrial_and_commercial_bank": 40,
                   "citic_bank": 40, "zijin_rural_commercial_bank": 40}

button_threshold = 5
