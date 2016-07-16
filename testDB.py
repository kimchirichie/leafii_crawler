from pymongo import MongoClient
import datetime
#import pprint
#import string
from WebCrawlLeafiipdf import get_html

client = MongoClient('mongodb://127.0.0.1:3001/meteor')

db = client.meteor

data = [{
	"_id":"waWjX44z8hVRxlsY1",
	"emails":[{"address":"sinr0202@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$uIl9n8BQQk0MBfjTlXccNeN9Xn3MCMOMaJ/rjSfJH9MWSeMXhiSze"
		}
	},
	"profile":{
		"firstName":"Richard",
		"lastName":"Sin",
		"url":"richardsin.com",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T09:17:23.242Z"
},
{
	"_id":"YLDFJ33eqCHDTGUtH",
	"emails":[{"address":"ttrzeng@uwaterloo.ca","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$Kp1oUU9UiKNc6E7iC.lhAebOzoQXPYrqIYQWU3OK0Q2OnRDS3Rxkq"
		}
	},
	"profile":{
		"firstName":"Talent",
		"lastName":"Zeng",
		"url":"talentzeng.com",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T09:17:23.242Z"
},
{
	"_id":"AclqR3s049ytEIx4E",
	"emails":[{"address":"Artist.kaylee@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$JlUjCMp3VeASXQClOlBg3.PyhI.7bdso6fE/Ibbh.6RZIrrD.NbqW"
		}
	},
	"profile":{
		"firstName":"Kaylee",
		"lastName":"Lock-O'Connor",
		"url":"www.artistkaylee.wix.com/kloc",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T09:15:44.086Z"
},
{
	"_id":"p4ndwfOKRnpCs6s0M",
	"emails":[{"address":"dmdque@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$8kZtE/bxVQEy8ovJ4zcqpOYGms3iv7Gptoo9eKmEANx5d5VHgPhFW"
		}
	},
	"profile":{
		"firstName":"Daniel ",
		"lastName":"Que",
		"url":"www.danielque.me",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T09:16:32.940Z"
},
{
	"_id":"HmMWQdwsnPoigdrkT",
	"emails":[{"address":"tcfraser@tcfraser.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$j4yx8uJ.JE1zzUMJyyDTOey92D.iksI3.6YHlY3a5scsKcYrAEdq6"
		}
	},
	"profile":{
		"firstName":"Tc",
		"lastName":"Fraser",
		"url":"www.tcfraser.com",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T09:16:59.324Z"
},
{
	"_id":"Si4iZazXlP9EHb2FJ",
	"emails":[{"address":"tnyqu6@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$U6Y9f1Ob1ttAAf54O3s4.OEHUxMSHEEkKvJB/kZW.qo3fTrf4Nb5i"
		}
	},
	"profile":{
		"firstName":"Tony",
		"lastName":"Qu",
		"url":"www.tonyqu.com",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T09:17:52.862Z"
},
{
	"_id":"n6kM5DHEmqQ0DITG8",
	"emails":[{"address":"abhijith.ramalingam@live.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$z7MV2S0sAEtupZkffpjKkOWPTkvtRKmwxIn7DsVUhIbZc4FRjcoVy"
		}
	},
	"profile":{
		"firstName":"Abhijith",
		"lastName":"Ramalingam",
		"url":"www.abhijith.info",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T09:19:25.870Z"
},
{
	"_id":"eU8WSv9jNa26e9BTb",
	"emails":[{"address":"meghan.yabsley@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$NqMvlKVpJJSMc.ejs.AsYOvYHWOdcOogBn0tub7lIQWu6X3UxTv1G"
		}
	},
	"profile":{
		"firstName":"Meghan",
		"lastName":"Yabsley",
		"url":"myabsley.com/",
		"location":"Toronto/Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T09:20:05.640Z"
},
{
	"_id":"sopT6PqH2n6um4J2K",
	"emails":[{"address":"craigaloewen+leafii@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$givmdysPjUGssE.2z7sOtu.o0GRRYEAST9YK5vcCPFW8wt6.FQIqu"
		}
	},
	"profile":{
		"firstName":"Craig",
		"lastName":"Loewen",
		"url":"www.craigloewen.com",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T09:20:37.153Z"
},
{
	"_id":"u7VtVsVjBGoSLe9U7",
	"emails":[{"address":"bevzabawskyj@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$bI8EwB5uYbbY7cqkdI8DtO9HB0APB/ehN6wQ5xMt/tO6NPxduNO1u"
		}
	},
	"profile":{
		"firstName":"Beverly",
		"lastName":"Zabawskyj",
		"url":"Bevzabawskyj.wix.com/portfolio",
		"location":"Toronto",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T09:21:19.513Z"
},
{
	"_id":"2APRl2tRk0R2AHMaz",
	"emails":[{"address":"olivia_w_chan95@hotmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$aTHqdpKnRztv7wqRLsKqhuVNSzXwugZjgHI/hPz4ZAI3dcBY0eR8S"
		}
	},
	"profile":{
		"firstName":"Olivia",
		"lastName":"Chan",
		"url":"www.oliviachandesign.com",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T09:21:49.797Z"
},
{
	"_id":"C69EDgl3BMLA5VMMg",
	"emails":[{"address":"sameer.khan@uwaterloo.ca","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$CvNNRH5RjfdCr5LXpKVcTezOGEVleTvadKFFIk..mtTT764Zum51K"
		}
	},
	"profile":{
		"firstName":"Sameer ",
		"lastName":"Khan",
		"url":"linkedin.com/in/samkhan13",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T14:05:28.722Z"
},
{
	"_id":"QlTZysShEhLmEID0H",
	"emails":[{"address":"me@andrewparadi.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$hEXhv3FcrphZt9dvhJWB3e9UFu0zU7ZRJ8C4MDJ5bG02ynwIcpN3."
		}
	},
	"profile":{
		"firstName":"Andrew",
		"lastName":"Paradi",
		"url":"andrewparadi.com",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T14:06:11.702Z"
},
{
	"_id":"JNaICPMhHAxzQPbEz",
	"emails":[{"address":"cassandrachan1@hotmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$q3h5b0kv3m/CcN5ETc8qWOnWGHYDBVfGvW6q8G5sxligR8U9rcPx2"
		}
	},
	"profile":{
		"firstName":"Cassandra",
		"lastName":"Chan",
		"url":"www.chancassandra.com",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T14:16:46.980Z"
},
{
	"_id":"RZMB2ue3vN98JDFSi",
	"emails":[{"address":"kntraian@uwaterloo.ca","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$HGV0hg7apzBiCglhtVjk6eSEEN1yWw/6ysMfKHFV81/wgGksPFPxy"
		}
	},
	"profile":{
		"firstName":"Krysta",
		"lastName":"Traianovski",
		"url":"www.linkedin.com/in/krystatraianovski",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T15:18:13.669Z"
},
{
	"_id":"ZhzuVyjBrjLp094Wh",
	"emails":[{"address":"lorna.qin@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$rNegzKIBUxtBrDdmVvOGeucq4CyNCpEZ/5F3ccsX7NwkXZDtZULY2"
		}
	},
	"profile":{
		"firstName":"Lorna",
		"lastName":"Qin",
		"url":"www.lornaqin.com",
		"location":"Scarborough",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T16:23:41.423Z"
},
{
	"_id":"LI4FvIxQlhVNHdL9K",
	"emails":[{"address":"aaron@pixelbirddesign.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$JBDJq7oQHHTsR9PnO0IF2.CwDthnTnaPRnc2axvSqae.ygEiYZDWe"
		}
	},
	"profile":{
		"firstName":"Aaron",
		"lastName":"Wong",
		"url":"www.pixelbirddesign.com",
		"location":"Toronto",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T16:42:27.248Z"
},
{
	"_id":"O4xxPveqDdIOnfskI",
	"emails":[{"address":"yongli.iss2016@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$S2EutpDfi2ZTfRYmZrL72Ou5tAt4MI2aPc4pBJsqqSVm83Kj67NNK"
		}
	},
	"profile":{
		"firstName":"Yongli",
		"lastName":"Jiang",
		"url":"yljiang.github.io",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T17:40:03.417Z"
},
{
	"_id":"PRT4y57bJGzECbYn8",
	"emails":[{"address":"mbeylin@uwaterloo.ca","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$csbxD8WtNw7tx0Za4fqpqudnrWo7tUz2AxBFiyme6ZW9Wv9p/v6Oa"
		}
	},
	"profile":{
		"firstName":"Mark",
		"lastName":"Beylin",
		"url":"beylin.ca",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-20T23:09:05.227Z"
},
{
	"_id":"osVlowrAVHrjjCCld",
	"emails":[{"address":"root@graham-robertson.ca","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$r7YEuAtWgkunAa0UxT9JV.mdDI56XBf7S0P7XJ3TQd0VdOK7fqJVq"
		}
	},
	"profile":{
		"firstName":"Graham",
		"lastName":"Robertson",
		"url":"www.graham-robertson.ca",
		"location":"Toronto",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-21T20:22:55.228Z"
},
{
	"_id":"aNi4DRcQ2yNBdaeGL",
	"emails":[{"address":"jack.teng.li@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$K9/XYdqBJlqqND4WLL4nzurVGRRzvTK3uDZnMAhTcEEBlU0SYCW26"
		}
	},
	"profile":{
		"firstName":"Jack",
		"lastName":"Li",
		"url":"www.jacktli.com",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-22T01:40:18.213Z"
},
{
	"_id":"8rnxriXqrTXdJUo0x",
	"emails":[{"address":"i4leung@uwaterloo.ca","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$i08s93t6E50.SuI1oQBbju8K73hHtJU/2Rhy16SFc2LElIU9IYOxC"
		}
	},
	"profile":{
		"firstName":"Ian",
		"lastName":"Leung",
		"url":"www.ianmhleung.com",
		"location":"Markham",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-22T01:57:23.382Z"
},
{
	"_id":"8kzHqMI6CTKwX151m",
	"emails":[{"address":"navjotspanesar+leafii@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$Ln5VZFR/pbW.P/5T9QfYD.cIrtQJOFmYxAZRRQuz71xof8ag70SSy"
		}
	},
	"profile":{
		"firstName":"Navjot",
		"lastName":"Panesar",
		"url":"navjotpanesar.com/#/",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-22T02:33:45.856Z"
},
{
	"_id":"b21swjczAm6MwO7sD",
	"emails":[{"address":"hello@krispenney.me","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$dBMqL6XjwANO/VWgOnP.aOS0EkklWwqEGNQDGG5YXPXv/yjR9wgpi"
		}
	},
	"profile":{
		"firstName":"Kris",
		"lastName":"Penney",
		"url":"krispenney.me",
		"location":"Paris",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-22T05:29:34.788Z"
},
{
	"_id":"a3F6E62pdfE7kjEew",
	"emails":[{"address":"andrewihassan@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$RaU.YnzSOUopuP.eDf8DReVLChvPlV7kxNzsR.1YbsRGnPr9M13Cm"
		}
	},
	"profile":{
		"firstName":"Andrew",
		"lastName":"Hassan",
		"url":"www.andrewhassan.com",
		"location":"Toronto",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-22T13:33:06.733Z"
},
{
	"_id":"ef5XTEJwWX1QajBCh",
	"emails":[{"address":"spurrya@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$3tohveLJqF33fBBRyEd0pOcMLBhnfuS09uKKWa8gq3SgYjjeDEXa6"
		}
	},
	"profile":{
		"firstName":"Spurrya",
		"lastName":"Jaggi",
		"url":"spurrya.com",
		"location":"Mississauga",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-22T23:04:08.120Z"
},
{
	"_id":"L1sMSGYEPB9OGCMa2",
	"emails":[{"address":"rntsang@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$n7fOa7LZ.5D/IUCSNdIfmu2sTPCoELPefYlv2BpxEydCrUKArr76S"
		}
	},
	"profile":{
		"firstName":"Ron",
		"lastName":"Tsang",
		"url":"www.rontsang.com",
		"location":"waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-24T00:59:50.212Z"
},
{
	"_id":"uz1HIO5OpdH540GuG",
	"emails":[{"address":"ashwintennis@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$rAFZQ4dYh.SUmQRj7PN7C.tAHWZGRMO1pS5hKIUe.7umuTUkqr.lq"
		}
	},
	"profile":{
		"firstName":"Ashwin",
		"lastName":"Krishnan",
		"url":"www.Ashwinkrishnan.me",
		"location":"Brossard",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-24T23:17:59.674Z"
},
{
	"_id":"zPHT7tmu2c8UHuMif",
	"emails":[{"address":"howdy@hussainabbas.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$D84cxxXgzqClpKDJlVyko.9YOa89Na7hOArjQ20skrQ5Zlq4qPkDq"
		}
	},
	"profile":{
		"firstName":"Hussain",
		"lastName":"Abbas",
		"url":"hussainabbas.com",
		"location":"Vaughan",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-25T14:49:13.057Z"
},
{
	"_id":"x2iKJwmEBLlFo7Zyh",
	"emails":[{"address":"akennewe@uwaterloo.ca","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$hm8LiKeJzO/U0mfg6SnOpOEMRnDaAcBl1Hii7uNrrbv/K./1IANgW"
		}
	},
	"profile":{
		"firstName":"Adam",
		"lastName":"Kenneweg",
		"url":"www.akenneweg.com",
		"location":"Barrie",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-26T00:33:55.805Z"
},
{
	"_id":"oPpD2qlXDThcQjvxL",
	"emails":[{"address":"jsypkes30@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$Hfi5vDxp0liGIo2P.6e6FO8dXXX5sItiGdIpCht9qQ/qyi3n.Ndw2"
		}
	},
	"profile":{
		"firstName":"Joel",
		"lastName":"Sypkes",
		"url":"issuu.com/joelsypkes/docs/portfolio_jsypkes",
		"location":"Guelph",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-26T00:36:43.064Z"
},
{
	"_id":"vHKkkFFUwxVSZ6Xnu",
	"emails":[{"address":"iam@ericaxu.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$szZbPZRyCdFlVK26TqKK6uXvv31WX8kvXcCVNUqdK/szysDjVKIIu"
		}
	},
	"profile":{
		"firstName":"Erica",
		"lastName":"Xu",
		"url":"www.ericaxu.com",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-26T00:43:09.643Z"
},
{
	"_id":"lv7ISRkEU5sh8tKxb",
	"emails":[{"address":"s5abdull@uwaterloo.ca","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$SaiPV9v0T6QJJGv9k3zKzuOuqkkwQzcqFodxdsgPbIM17WWHEdskW"
		}
	},
	"profile":{
		"firstName":"Shameel",
		"lastName":"Abdullah",
		"url":"meeoh.gihub.io",
		"location":"Cambridge",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-27T20:19:47.652Z"
},
{
	"_id":"zxXnYPnStDwPQ7ZxO",
	"emails":[{"address":"stevenho1103@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$yH2zDkjzqD9TiYfAAJj.sOV8C9/suts1VKFtJenoGe8YLa3NCApGm"
		}
	},
	"profile":{
		"firstName":"Steven",
		"lastName":"Ho",
		"url":"www.stevenhodesigns.com",
		"location":"Vancouver",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-27T20:29:58.434Z"
},
{
	"_id":"My4CcFHikWoGcM3Fq",
	"emails":[{"address":"tmondol@uwaterloo.ca","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$EElQdYzVqwSttZfTFmYZ/OG1THbvNdV2zQpwTOkp4dI75pvo2Oebm"
		}
	},
	"profile":{
		"firstName":"Tiasa",
		"lastName":"Mondol",
		"url":"tiasauwcs10.ca",
		"location":"Kitchener",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-28T19:25:41.363Z"
},
{
	"_id":"NbikkFDhkvQC1tLPF",
	"emails":[{"address":"michellersin@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$mw5Jp86ve2xmja/60QiNiuBOKYDQpiADJYsglfDF43CdZTRXLigBK"
		}
	},
	"profile":{
		"firstName":"Michelle",
		"lastName":"Sin",
		"url":"www.redefinewaste.com/",
		"location":"Markham",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-05-31T00:46:58.627Z"
},
{
	"_id":"Gf6V5osUacSn3ERLz",
	"emails":[{"address":"j283chen@live.ca","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$MxctU7hsZtdlPHrWzuCy0.ET4AjH8Zvo3ELiedeQsJq6Fc45kpi1a"
		}
	},
	"profile":{
		"firstName":"Jason",
		"lastName":"Chen",
		"url":"jchenengineering.com",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-06-01T01:10:00.039Z"
},
{
	"_id":"LeOt6WLGO0YsedxdU",
	"emails":[{"address":"adamimtz@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$2EOvTSm5zzX3rbqGHDDC0.p5gWnGyfJxRLkqZH80Vhq/W5dTeqZEq"
		}
	},
	"profile":{
		"firstName":"Adam",
		"lastName":"Imtiaz",
		"url":"a-imtz.github.io",
		"location":"Innisfil",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-06-02T23:48:34.445Z"
},
{
	"_id":"3kPm9adILhL21zB0h",
	"emails":[{"address":"tianyuan.zhao@utoronto.ca","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$MrI/3GPrJMEBCfT9kWOaGe2ubdJ3WGIoH1kPLjuVWMT.HfuUTFsdi"
		}
	},
	"profile":{
		"firstName":"Tian-Yuan",
		"lastName":"Zhao",
		"url":"tianyuanzhao.me",
		"location":"Toronto",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-06-04T03:53:49.504Z"
},
{
	"_id":"fvzbAsf0Cwjxq8Jmk",
	"emails":[{"address":"sebastian.kolosa@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$sCiM09sQMwnlc/I6kY1V7uobvbZQZQeV0Lbx97/nKCqTUFc4i9RRm"
		}
	},
	"profile":{
		"firstName":"Sebastian",
		"lastName":"Kolosa",
		"url":"www.sebastiankolosa.me",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-06-07T01:07:36.359Z"
},
{
	"_id":"a9DS90NNHQaZ51kp4",
	"emails":[{"address":"jenna.ayu@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$Xmel2bQh5.5nb2xdPtVbLerReK1ImHUhzZ6iT4Rl.cGEMIvRgUwia"
		}
	},
	"profile":{
		"firstName":"Jenevieve",
		"lastName":"Ayuste",
		"url":"jenevievea.wix.com/portfolio",
		"location":"Waterloo",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-06-09T16:29:12.553Z"
},
{
	"_id":"7vMp0ySvViaHniZ3g",
	"emails":[{"address":"mvjoshi@uwaterloo.ca","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$UMR5ohtQraHwrqB5hZLUY.KYK49ZnvemT1T6S6K5yKXbD1NuMugY."
		}
	},
	"profile":{
		"firstName":"Manas",
		"lastName":"Joshi",
		"url":"manas-joshi-uw.github.io",
		"location":"Pickering",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-06-09T16:30:22.083Z"
},
{
	"_id":"xy3TeX9eAazFR8keq",
	"emails":[{"address":"david.s.moscoe@gmail.com","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$f/40uVosnn.fkW/VYVxskujv26dLQtv3wv7wFExqxgyiUP0zS7fmy"
		}
	},
	"profile":{
		"firstName":"David",
		"lastName":"Moscoe",
		"url":"moocowunicycles@gmail.com",
		"location":"Toronto",
		"occupation": "",
		"available": False
	},
	"createdAt":"2016-06-09T16:37:34.893Z"
},
{
	"_id":"3ooBwhm021c7IUv5G",
	"emails":[{"address":"k24luu@uwaterloo.ca","verified":False}],
	"services":{
		"password":{
			"bcrypt":"$2a$10$r.BLr33/mYKC4MMBUtG6BOWUiJsfSSY7wxcnR/A3gdl.2b1Y1Vt1K"
		}
	},
	"profile":{
		"firstName":"Kelvin",
		"lastName":"Lau",
		"url":"www.linkedin.com/in/ykelvinlau",
		"location":"Mississauga/Toronto/Waterloo",
		"occupation": "Full Stack Software Engineer",
		"available": False
	},
	"createdAt":"2016-06-17T23:28:28.653Z"
}]

key_dict = db.keywords
for i in range(len(data)):
	data_temp = data[i]
	url_temp = (data_temp.get("profile").get("url"))
	id_temp = (data_temp.get("_id"))

	tags = get_html(url_temp)

	key_db = {"keywords": tags, "url": url_temp, "user_id": id_temp}

	key_dict_id = key_dict.insert_one(key_db).inserted_id
	#print (key_dict_id)




