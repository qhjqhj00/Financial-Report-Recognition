

# free cash flow to firm
def FCFF(Int, FCInv, tax_rate, CFO=None, NI=None,NCC=None):
    if CFO is not None:
        return CFO+(Int*(1-tax_rate)-FCInv)
    if NI is not None and NCC is not None:
        return NI+NCC+(Int*(1-tax_rate)-FCInv)


def net_borrowing(debt_issued,debt_repaid):
    return debt_issued-debt_repaid


# free cash flow to equity
def FCFE(CFO, FCInv, net_borrowing):
    return CFO-FCInv+net_borrowing


class cash_flow_statement:
    def __init__(self,
                 net_income, gain_f_i=0,
                 operating_asset_acount=0,
                 operating_liability_acount=0,
                 non_cash_change=0,
                 non_cash_revenue=0
                 ):
        self.net_income = net_income
        self.operating_asset_acount = operating_asset_acount
        self.operating_liability_acount = operating_liability_acount
        self.non_cash_change = non_cash_change
        self.non_cash_revenue = non_cash_revenue
        self.gain_f_i = gain_f_i
        self.CFO = net_income-operating_asset_acount+operating_liability_acount+non_cash_change-non_cash_revenue

    def FCFF(self, Int, FCInv, tax_rate):
        return self.CFO+(Int*(1-tax_rate)-FCInv)

    def FCFE(self,FCInv, net_borrowing):
        return self.CFO-FCInv+net_borrowing

    def cf2rev(self,net_revenue):
        """cash flow to revenue"""
        return round(self.CFO/net_revenue,4)

    def c_roa_r(self,average_total_asset):
        """cash return-on-assets ratio"""
        return round(self.CFO / average_total_asset, 4)

    def c_roe_r(self,average_total_equity):
        """cash return-on-equity ratio"""
        return round(self.CFO / average_total_equity, 4)

    def c2inc_r(self, operating_income):
        """cash to income ratio"""
        return round(self.CFO / operating_income, 4)

    def cf_per_s(self,pr_di,com_s):
        """cash flow per share"""
        return round(self.CFO -pr_di / com_s, 4)

    def debt_conv(self,total_debt):
        return round(self.CFO / total_debt, 4)

    def int_conv(self,int_paid,tax_paid):
        """interests converge"""
        return round((self.CFO+int_paid+tax_paid)/int_paid,4)

    def reinvestment(self,cash_lta):
        """
        :param cash_lta: cash paid for long-term assets
        :return: reinvestment
        """
        return round(self.CFO/cash_lta,4)

    def debt_payment(self,cash_ltdr):
        """
        :param cash_ltdr: cash long-term debt repayment
        :return: debt_payment
        """
        return round(self.CFO/cash_ltdr,4)

    def devidend_payment(self,div_paid):
        """
        :param div_paid: dividend paid
        :return: devidend_payment
        """
        return round(self.CFO / div_paid, 4)

    def inv_fin(self,cf_if):
        """
        :param cf_if: cash flow from investing and financial activities
        :return: investing and financing
        """
        return round(self.CFO / cf_if, 4)
    
