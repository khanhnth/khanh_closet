from flask import Flask,render_template

# import mongoengine
# from mongoengine import Document,StringField
# host = "ds021943.mlab.com"
# port = 21943
# db_name = "my_closet"
# user_name = "khanhnth"
# password = "hallo296"
# mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

app = Flask(__name__)

class Outfit:
    def __init__(self,title,img,des):
        self.title = title
        self.img = img
        self.des = des

outfit1 = Outfit('Contemporary Pleated-Back Crepe Shirt','http://www.forever21.com/images/4_full_750/00113493-03.jpg',"Forever 21 Contemporary - Finely and femininely tailored, this shirt is cut from a crepe that's just a touch sheer, with a boxy silhouette and hidden button placket. Our favorite detail? The pretty pleated back.")
outfit2 = Outfit('Contemporary Scarf Print Top','http://www.forever21.com/images/7_additional_750/00132544-02.jpg',"Forever 21 Contemporary - A short-sleeved top that features an allover abstract scarf print, a striped trim, and a contrast ribbed crew neck. Matching shorts available.")
outfit3 = Outfit('Contemporary Floral Shift Dress','http://www.forever21.com/images/1_front_750/00205195-01.jpg',"Forever 21 Contemporary - A crepe woven shift dress with an allover abstract floral print, a sleeveless cut, a round neckline, and a buttoned keyhole back.")

outfits = [outfit1,outfit2,outfit3]

# class Outfit(Document):
#     title = StringField()
#     img = StringField()
#     des = StringField()

@app.route('/')
def closet():
    return render_template('closet.html',outfits = outfits)


if __name__ == '__main__':
    app.run()
