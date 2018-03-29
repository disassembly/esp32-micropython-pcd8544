class CN_UTF8:
    """docstring for CN_UTF8"""
    #key:values
    #key: ʹ�ú��ֵ�UTF-8��
    #values: 16*16
    #   [0] 8*16 �ϰ벿��
    #   [1] 8*16 �°벿��
    UTF8_CHINESE = {
        '1':[
	           [0x00,0x00,0x20,0xE0,0xE0,0x20,0x00,0x00],
		    [0x00,0x00,0x00,0x3F,0x3F,0x10,0x00,0x00]
          ],#1_reversed
	'2':[
		[0x00,0x60,0x60,0x20,0xA0,0xE0,0x60,0x00],
		[0x00,0x1C,0x3E,0x23,0x21,0x38,0x18,0x00]
	],#2_reversed
	'3':[
		[0x00,0xC0,0xE0,0x20,0x20,0x60,0x40,0x00],
		[0x00,0x1D,0x3F,0x22,0x22,0x30,0x10,0x00]
	],#8_reversed
	'4':[
		[0x00,0xA0,0xE0,0xE0,0xA0,0x80,0x80,0x00],
		[0x00,0x00,0x3F,0x3F,0x0E,0x07,0x01,0x00]
	],#4_reversed
	'5':[
		[0x00,0xC0,0xE0,0x20,0x20,0xE0,0xC0,0x00],
		[0x00,0x23,0x27,0x24,0x24,0x3E,0x3E,0x00]
	],#5_reversed
	'6':[
		[0x00,0xC0,0xE0,0x20,0x20,0xE0,0xC0,0x00],
		[0x00,0x13,0x37,0x24,0x36,0x1F,0x0F,0x00]
	],#6_reversed
	'7':[
		[0x00,0x00,0x00,0xE0,0xE0,0x00,0x00,0x00],
		[0x00,0x30,0x3E,0x2F,0x21,0x30,0x30,0x00]
	],#7_reversed
       '8':[
		[0x00,0xC0,0xE0,0x20,0x20,0xE0,0xC0,0x00],
		[0x00,0x1D,0x3F,0x22,0x22,0x3F,0x1D,0x00]
	],#8_reversed
	'9':[
		[0x00,0x80,0xC0,0x60,0x20,0x60,0x40,0x00],
		[0x00,0x1F,0x3F,0x23,0x21,0x3F,0x1E,0x00]
	],#9_reversed
       '0':[
		[0x00,0xC0,0xE0,0x20,0x20,0xE0,0xC0,0x00],
		[0x00,0x1F,0x3F,0x20,0x20,0x3F,0x1F,0x00],
	],#0_reversed
	'x':[
		[0x00,0x10,0x10,0x50,0x50,0x50,0xF0,0xF0,0x50,0x50,0x50,0x90,0x90,0x00],
		[0x00,0x00,0xF9,0xF9,0xA9,0xA9,0xAF,0xAF,0xA9,0xA9,0xFB,0xFB,0x00,0x00]
	],#xing_reversed
	'y':[
		[0x00,0xF0,0xF0,0x10,0xE0,0xF0,0x90,0xB0,0xA0,0x80,0xA0,0xB0,0x90,0x00],
		[0x00,0x7F,0x7F,0x49,0x7F,0x7F,0x20,0xFF,0xFF,0x2A,0xFF,0xFF,0x20,0x00]
	],#qi_reversed

	'a':[
		[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
		[0x00,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x00]
	],#yi_reversed
	'b':[
		[0x00,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x00],
		[0x00,0x00,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x00,0x00]
	],#er_reversed
	'c':[
		[0x00,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x00],
		[0x00,0x00,0x40,0x42,0x42,0x42,0x42,0x42,0x42,0x42,0x42,0x40,0x00,0x00]
	],#san_reversed
	'd':[
		[0x00,0xF0,0xF0,0x20,0x20,0x20,0x20,0x20,0x20,0xA0,0xF0,0xF0,0x00,0x00],
		[0x00,0x7F,0x7F,0x41,0x7F,0x7E,0x40,0x7E,0x7F,0x41,0x7F,0x7F,0x00,0x00]
	],#si_reversed
	'e':[
		[0x00,0x10,0x10,0xF0,0xF0,0x10,0x10,0x10,0x90,0xF0,0x70,0x10,0x10,0x00],
		[0x00,0x00,0x40,0x47,0x47,0x44,0x44,0x7C,0x7F,0x47,0x44,0x44,0x40,0x00]
	],#wu_reversed
	'f':[
		[0x00,0x30,0xF0,0xC0,0x00,0x00,0x00,0x00,0x00,0xC0,0xE0,0x30,0x10,0x00],
		[0x00,0x08,0x08,0x09,0x0B,0x0A,0x68,0xE8,0x8B,0x0B,0x08,0x08,0x08,0x00]
	],#liu_reversed
	'g':[
		[0x00,0x00,0xF0,0xF0,0x20,0x20,0x20,0x20,0x20,0x20,0xF0,0xF0,0x00,0x00],
		[0x00,0x00,0x7F,0x7F,0x44,0x44,0x44,0x44,0x44,0x44,0x7F,0x7F,0x00,0x00]
	],#ri_reversed
	'm':[
		[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
		[0x00,0x02,0x02,0x02,0x02,0x02,0x02,0x02]
	],#-_reversed
	'n':[
		[0x00,0x00,0x00,0x00,0x20,0x20,0x00,0x00],
		[0x00,0x00,0x00,0x00,0x04,0x04,0x00,0x00]
	],#:_reversed    
    }
    #key ���ֵ�UTF-8��
    #isBottom ȷ������ǻ�ȡ ĳ���ֵ� �ϰ벿�֣�0�� �����°벿�֣�1��
    def get_chinese_utf8(self, key,isBottom = 0):
        values = self.UTF8_CHINESE[key]
        return values[isBottom]