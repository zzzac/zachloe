'''
Author: your name
Date: 2021-05-10 12:53:05
LastEditTime: 2021-05-10 13:54:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /undefined/Users/doctor/Documents/GitHub/zachloe/GRE_killer.py
'''
import random

list5 = {
    'evanescent': '短暂的',
    'free-for-all': '混战',
    'rudimentary': '基本的',
    'bustling' : '忙乱的',
    'prioritize' : '优先',
    'envision' : 'think of, 想象',
    'circumscribe' : 'limit the amount of, confine',
    'reminiscent' : 'remind of sth, 引起回忆的',
    'symmetrical' : '对称',
    'overthrow' : '推翻',
    'juvenuile' : '幼稚',
    'elude' : '逃跑(escape)，使无法理解（puzzle），使无法得到',
    'jettison' : '拒绝，放弃，reject',
    'detriment' : '破坏',
    'baroque' : '奢华',
    'quixotic' : '不切实际，变化多端',
    'mockery' : '嘲笑',
    'tactful' : '圆滑，为他人着想，careful not to offend or upset',
    'trendy' : 'fashion',
    'subsidize' : '赞助',
    'numious' : '超自然，supernatural',
    'anomalous' : '不寻常的',
    'mawkish' : '恶心做作',
    'invidious' : '令人反感',
    'austere' : '朴素的，严肃的',
    'impede' : '阻碍,impediment',
    'frank' : '真诚的',
    'disjunction' : '分裂，分离',
    'finicky' : '挑剔的',
    'hazardous' : '危险的',
    'chicanery' : '欺骗，诡计',
    'verifiable' : '可验证的',
    'demonstrable' : '可证明的',
    'pertinacious' : 'holding tenaciously to a purpose, belief, 坚持',
    'scarce' : '缺乏的',
    'lavish' : '奢华的',
    'sanguine' : '乐观的',
    'waver': '摇摆不定',
    'engender' : '产生',
    'elusive' : '难懂，难以捉摸',
    'ponder' : '沉思',
    'poliferate' : '快速增长',
    'paucity' : '少量',
    'univocal' : '唯一的，明确的',
    'dejected' : '沮丧的',
    'surplus': '多余',
    'impertinent' : '粗鲁的',
    'one-of-a-kind' : '独一无二',
    'apropos' : '合适的',
    'ingratiate' : '讨好',
    'concoct' : '编造',
    'disgorge': '吐',
    'baseless' : '没有根据',
    'momentary' : '短暂的',
    'debilitate' : '虚弱',
    'acute' : '敏锐',
    'resent' : '憎恨',
    'delightful' : '开心的',
    'decisive' : '坚定地，果断的',
    'testimony' : '证词',
    'nominal' : '名义上',
    'simultaneously' : '同时',
    'monotonous' : '单调',
    'divination' : '预言占卜',
    'virtuosity' : '精湛的技艺',
    'manifest' : '展现',
    'purview' : '视野',
    'annex' : '附加',
    'shriek': '尖叫',
    'ephemeral' : '短暂',
    'erudite' : '博学',
    'plague' : '瘟疫',
    'counterintuitive' : '违反常理，反直觉',
    'intriguing' : '非常有趣',
    'magnanious' : '大度，慷慨',
    'untether' : '释放脱离，divorce',
    'formulaic' : '刻板俗套',
    'gambit' : '计划',
    'vivacious' : '活力四射',
    'stratify' : '分层',
    'exceptional' : '不寻常的',
    'slump' : '急速下跌',
    'pessimistic' : '悲观的',
    'dilute' : '稀释，减轻',
    'palatable' : '美味的',
    'stagnate' : '停滞',
    'esoteric' : '难懂',
    'befuddle' : '困惑',
    'deliberate' : '深思熟虑，故意',
    'antithesis':'对立的',
    'valediction' : '告别',
    'hamstring' : '损坏',
    'complacent' : '自满',
    'hinder' : '阻碍',
    'fomidable' : '令人惊叹，可怕，艰巨',
    'impenetrable' : '无法穿透，难懂',
    'obstrude' : '闯入，强迫',
    'debunk' : '拆穿',
    'umbrage' : '不悦',
    'affinity' : '偏好，相似',
}


list5_h = {
    'detriment' : '破坏',
    'defuddle' : "困惑",
    'untether' : "divoce",
    'plague' : "瘟疫",
    'affinity' : "相似",
    'shriek' : "尖叫",
    'invidious' : "令人反感",
    'paucity' : "少量",
    'evanescent' : "短暂的",
    'ingratiate' : "讨好",
    'hinder' : "阻碍",
    'dilute' : "减轻，稀释",
    'debunk' : "拆穿",
    'disgorge' : "吐",
    'deblitate' : "虚弱",
    'elusive' : "难以捉摸",
    'complacent' : "自满",
    'umbrage' : "不悦",
    'valediction' : "告别",
    'stagnate' : "停滞",
    'impenetrable' : "难懂",
    'ephemeral' : "短暂",
    'antithesis' : "对立的",
    'deliberate' : "故意",
    'impertinent' : "粗鲁的",
    'testimony' : "证词",
    'impede' : "阻碍",
    'divination' : "预言占卜",
    'magnanious' : "大度的",
    'hamstring' : "损坏"
}

wordlists = {"list5": list5,
            "list5_h": list5_h}

if __name__ == '__main__':
    selected_wordlist = 'list' + input('Select a wordlist: ')
    while selected_wordlist not in wordlists.keys():
        print('Did not find the wordlist: ',selected_wordlist,'please re-enter')
        selected_wordlist = 'list' + input('Select a wordlist: ')
    print('You selected: ', selected_wordlist)
    wordlist = wordlists[selected_wordlist]
    keys = list(wordlist.keys())
    tested = []
    input('press any key to continue. ctrl+c to break')
    while 1:
        r = random.randint(0, len(keys)-1)
        if r in tested:
            continue
        input('')
        print('Question', len(tested)+1, ':', keys[r])
        input('')
        print(wordlist[keys[r]])
        tested.append(r)