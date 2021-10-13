class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        pre_res_dict = {}

        for cpdomain in cpdomains:
            cnt_domain_pair = cpdomain.split(' ')
            cnt = int(cnt_domain_pair[0])
            domain = cnt_domain_pair[1]

            domain_in_lst = domain.split('.')
            domain_len = len(domain_in_lst)
            for i in range(domain_len):
                cur_sub_domain = domain_in_lst[i:domain_len]
                cur_sub_domain_str = '.'.join(cur_sub_domain)
                if not pre_res_dict.get(cur_sub_domain_str, None):
                    pre_res_dict[cur_sub_domain_str] = cnt
                else:
                    pre_res_dict[cur_sub_domain_str] += cnt

        return ['{} {}'.format(val, key) for key, val in pre_res_dict.items()]
    
