from banglatts import BanglaTTS


bn = BanglaTTS(save_location='test')

print(bn("আমি বাংলা ভাষা পছন্দ করি।",voice='male'))