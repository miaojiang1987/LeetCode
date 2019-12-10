'''
给三个input, 点击广告的所有user id, 点击广告的所有用户的 [user_id, ip address], 
最终消费的用户[ip address, 在网站上购买的内容]
需要返回每个网站text 所对应的访问数和购买数
每个id在对应的网站上有购物行为，比如：
id = [1,2,3,4]
id_ip = [
[1, 127.1.1.1]
[2, 127.1.1.2]
[3, 127.1.1.3]
[4, 127.1.1.4]
]
ip_text = [
[127.1.1.1, "apple"]
[127.1.1.2, "banana"]
[127.1.1.3, "banana"]
[127.1.1.4, "apple"]
[127.1.1.4, "banana"]
]

output:
[
[127.1.1.1, 1, 1], 
[127.1.1.2, 1, 1],
[127.1.1.3, 1, 1],
[127.1.1.4, 1, 2],
 ]
 时间复杂度：O(n)
 空间复杂度：O(n)
'''

def online_shopping(ids, id_ips, ip_texts):
	websites = {ip: [None, None] for ip, text in ip_texts}
    for id, ip in id_ips:
        if websites[ip][0] is None:
            websites[ip][0] = 1
        else:
            websites[ip][0] += 1
    
    for ip, text in ip_texts:
        if websites[ip][1] is None:
            websites[ip][1] = 1
        else:
            websites[ip][1] += 1

    return websites
	
	
		
	
	
	