import dns.resolver

'''
验证邮箱地址合法性类
'''
class VerifyEmail:

    email_addrs = []
    def __init__(self, addrs):
        self.email_addrs = addrs

    def get_demain(self, addr):
        if '@' in addr:
            return addr.split('@')[1]
        return ''

    def verify(self):
        # 存储有效的邮箱地址
        valid_list = []
        for addr in self.email_addrs:
            demain = self.get_demain(addr)
            if len(demain) > 0 and self.is_existsMX(demain):
                valid_list.append(addr)
            else:
                continue
        return valid_list

    def wrong_demain(self):
        # 存储有效的邮箱地址
        wrong_list = []
        for addr in self.email_addrs:
            demain = self.get_demain(addr)
            if len(demain) > 0 and self.is_existsMX(demain):
                continue
            else:
                wrong_list.append(addr)
        return wrong_list

    # 查找邮箱服务器MX记录
    def is_existsMX(self, demain):
        try:
            answers = dns.resolver.query(demain, 'MX')
            res = [str(rdata.exchange)[:-1] for rdata in answers]
            if len(res) > 0:
                return True
            else:
                return False
        except:
            return False