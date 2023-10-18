# QN 1
catholic_martyrs = [
    "Achileo Kiwanuka", "Adolphus LudigoMukasa", "Ambrosius Kibuuka", "Anatoli Kiriggwajjo",
    "Andrew Kaggwa", "Antanansio Bazzekuketta", "Bruno Sserunkuuma", "Charles Lwanga",
    "Denis Ssebuggwawo", "Wasswa Gonzaga Gonza", "Gyavira Musoke", "James Buuzaabalyaawo",
    "John Maria Muzeeyi", "Joseph Mukasa Kizito", "Lukka Baanabakintu", "Matiya Mulumba",
    "Mbaga Tuzinde", "Mugagga Lubowa", "Mukasa Kiriwawanvu", "Nowa Mawaggali", "Ponsiano Ngondwe"
]

anglican_martyrs = [
    "Aaron Lubega", "Apollo Kivebulaya", "Eria Sebukyala", "Fredrick Kizza", "George Kizza",
    "James Hannington", "Janani Luwum", "Joseph Balikuddembe", "Kizito", "Mark Kakumba",
    "Matia Mulumba", "Nuhu Mbegu", "Robert Munyagayirwa", "Samwiri Mukasa", "Yefusa Namayanja",
    "Yohana Mukasa", "Yosefu Lugalama", "Yowana Kitaka", "Yowana Maria", "Mukasa"
]

#   QN 2
catholic_martyrs = list(set(catholic_martyrs))
anglican_martyrs = list(set(anglican_martyrs))

# QN 3
def martyr_count(name):
    if name in catholic_martyrs:
        return "Catholic"
    elif name in anglican_martyrs:
        return "Anglican"
    else:
        return "Not Found"

# QN 4
martyr_group = martyr_count("Kizito")
print("Group of Kizito:", martyr_group)
