
class activity_ratio:
    def __init__(self,sale,revenue,cost_g):
        self.sale =sale
        self.revenue = revenue
        self.cost_g = cost_g

    def rec_tnover(self,receivables):
        """
        average receivables are calculating by adding the beginning-of-year account value
        to the end-of-yeear account value than dividing the sum by two.
        :param receivables: average receivables
        :return: receivables turnover
        """
        return round(self.sale/receivables,4)

    def ave_coll_per(self,receivables):
        """
        :param rec_tnover: receivables turnover
        :return: average collection period
        """
        rec_tnover = self.rec_tnover(receivables)
        return round(365/rec_tnover,4)

    def inv_tnover(self,ave_inv):
        """
        :param ave_inv: average inventory
        :return: inventory turnover
        """
        return round(self.cost_g/ave_inv,4)

    def ave_inv_per(self,ave_inv):
        """
        :param inv_tnover: inventory turnover
        :return: aver
        """
        inv_tnover = self.inv_tnover(ave_inv)
        return round(365/inv_tnover,4)

    def purchse(self,end_inv,beg_inv):
        """

        :param end_inv:
        :param beg_inv:
        :return:
        """
        return round(end_inv-beg_inv+self.cost_g,4)

    @staticmethod
    def pay_tnover(purchase,ave_trad_pay):
        """
        :param purchase:
        :param ave_trad_pay: average trade payables
        :return: payable turnover
        """
        return round(purchase/ave_trad_pay,4)

    def ave_pay_per(self,purchase,ave_trad_pay):
        """
        :param purchase:
        :param ave_trad_pay: average trade payables
        :return: average payables period
        """
        pay_tnover = self.pay_tnover(purchase,ave_trad_pay)
        return round(pay_tnover/365,4)

    def tot_asset_tnover(self,tot_asset):
        """

        :param tot_asset: average total asset
        :return: total asset turnover
        """
        return round(self.revenue/tot_asset,4)

    def fixed_asset_tnover(self, fixed_asset):
        """

        :param fixed_asset: average total asset
        :return: fixed asset turnover
        """
        return round(self.revenue / fixed_asset, 4)

    @staticmethod
    def ave_wok_cap(asset,liab):
        """
        :param asset: average asset
        :param liab: average liabilities
        :return: average working capital
        """
        return round(asset-liab,4)

    def wok_cap_tnover(self, ave_wok_cap):
        """

        :param ave_wok_cap: average working capital
        :return: fixed asset turnover
        """
        return round(self.revenue / ave_wok_cap, 4)


class liquidity_ratio:
    def __init__(self,
                 cur_asset,
                 cur_liab,
                 cash=None,
                 mkb_sec=None,
                 rec=None,):
        """

        :param cur_asset: current asset
        :param cur_liab: current liabilities
        :param cash: cash
        :param mkb_sec: marketable securities
        :param rec: receivables
        """
        self.cur_asset = cur_asset
        self.cur_liab = cur_liab
        self.cash = cash
        self.mkb_sec = mkb_sec
        self.rec = rec

    def current(self):
        """
        best known measure of liquidity
        :return: current ratio
        """
        return round(self.cur_asset/self.cur_liab,4)

    def quick(self):
        """
        more stringent measure of liquidity
        :return: quick ratio
        """
        return round((self.cash+self.mkb_sec+self.rec)/self.cur_liab,4)

    def cash(self):
        """
        :return: cash ratio
        """
        return round((self.cash+self.mkb_sec)/self.cur_liab,4)

    def defen_int(self,ave_day_exp):
        """

        :param ave_day_exp: everage daily expenditures
        :return: 还剩几天
        """
        return round((self.cash+self.mkb_sec+self.rec)/ave_day_exp,4)

    @staticmethod
    def cash_conv_cyc(d_sales_outs,d_inv_on_hand,d_pay):
        """

        :param d_sales_outs: days sales outstanding
        :param d_inv_on_hand: days of inventory on hand
        :param d_pay: number of days of payables
        :return: cash conversion cycle
        """
        return round(d_sales_outs+d_inv_on_hand-d_pay,4)


class solvence_ratio:
    def __init__(self,debt):
        """

        :param debt: long-term debt + interest-bearing short term debt
        """
        self.debt = debt

    def d2equity(self,tot_equity):
        """

        :param tot_equity: total shareholders' equity
        :return: debt to equity
        """
        return round(self.debt/tot_equity,4)

    def d2capital(self, tot_equity):
        """

        :param tot_equity: total shareholders' equity
        :return: debt to capital
        """
        return round(self.debt/(self.debt+tot_equity),4)

    def d2asset(self,asset):
        """

        :param asset:total asset
        :return: debt to assets
        """
        return round(self.debt/asset,4)

    @staticmethod
    def fin_lev(ave_tot_ass,ave_tot_equ):
        """

        :param ave_tot_ass: average total assets
        :param ave_tot_equ: average total equity
        :return: financial leverage
        """
        return round(ave_tot_ass/ave_tot_equ,4)

    
    @staticmethod
    def int_cov(earn_bf_int_tax,int_pay):
        """

        :param earn_bf_int_tax: earnings before interest and tax
        :param int_pay: interest payment
        :return: initerest converage
        """
        return round(earn_bf_int_tax/int_pay,4)

    @staticmethod
    def fixed_char_cov(earn_bf_int_tax,int_pay,lease):
        """
        proper for companies that lease a large portion of asset
        :param earn_bf_int_tax: earnings before interest and tax
        :param int_pay: interest payment
        :param lease: lease payment
        :return: fixed charge coverage
        """
        return round((earn_bf_int_tax+lease)/(int_pay+lease),4)


class profitability_ratio:
    """profitability ratios measures the overall performance of the firm
    relative to revenues, assets, equity and capital"""
    def __init__(self,
                 net_income,
                 revenue,
                 ):
        self.net_income = net_income
        self.revenue = revenue

    def net_pro_mg(self):
        return round(self.net_income/self.revenue, 4)

    def gro_pro_mg(self, gro_prof):
        """

        :param gro_prof: gross profit
        :return: gross profit margin
        """
        return round(gro_prof/self.revenue,4)

    def op_pro_mg(self, op_inc):
        """

        :param op_inc: operating income
        :return: operating profit margin
        """
        return round(self.revenue/op_inc,4)

    def pret_mg(self, ebt):
        """

        :param ebt: earnings before tax
        :return: pretax margin
        """
        return round(ebt/self.revenue,4)

    def roa_vanilla(self,ave_tot_ass):
        """

        :param ave_tot_ass: average total assets
        :return: return on assets
        """
        return round(self.net_income/ave_tot_ass,4)

    def roa(self,ave_tot_ass,int, tax_rate):
        """

        :param ave_tot_ass: average total asset
        :param int: interest
        :param tax_rate: tax rate
        :return: return on assets
        """
        return round((self.net_income+int*(1-tax_rate))/ave_tot_ass,4)

    def op_roa(self,op_in,ave_tot_ass):
        """

        :param op_in: operating income
        :return: operating return on assets
        """
        return round(op_in/ave_tot_ass,4)

    def roe(self,ave_tot_eq):
        """

        :param ave_tot_eq: average total equity
        :return: return on equity
        """
        return round(self.net_income,ave_tot_eq)

    def ro_common_e(self,ave_com_eq,pref_div=0):
        """

        :param ave_com_eq: average common equity
        :param pref_div: preferred dividends
        :return: return on common equity
        """
        return round(((self.net_income-pref_div)/ave_com_eq),4)


class dupont:
    def __init__(self,net_inc,rev,eq,ave_tot_ass):
        self.net_inc = net_inc
        self.rev = rev
        self.ave_tot_ass = ave_tot_ass
        self.eq = eq

        self.net_pr_mg = round(net_inc/rev,4)
        self.ass_tnover = round(rev/ave_tot_ass,4)
        self.lvg_ratio = round(ave_tot_ass/eq,4)

    def dupont_result(self):
        return round(self.net_pr_mg*self.ass_tnover*self.lvg_ratio,4)


class dupont_v1:
    def __init__(self,net_inc,ebt,ebit,rev,ave_ass,ave_eq):
        self.tax_burden = round(net_inc/ebt,4)
        self.interest_burden = round(ebt/ebit,4)
        self.ebit_burden = round(ebit/rev,4)
        self.ass_tnover = round(rev/ave_ass,4)
        self.fin_lvg = round(ave_ass/ave_eq,4)

    def dupon_result(self):
        return round(self.tax_burden*self.interest_burden*self.ebit_burden*self.ass_tnover*self.fin_lvg,4)

def sus_growth_rate(rr,roe):
    return round(rr*roe,4)

def retation_rate(net_inc_com,div):
    """

    :param net_inc_com: net income available to common
    :param div: dividend
    :return: rr
    """
    return round((net_inc_com-div)/net_inc_com,4)

def coefficient_variation(standard_deviation,mean):
    return round(standard_deviation/mean,4)



