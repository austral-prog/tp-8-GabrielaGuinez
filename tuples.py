def get_coordinate(record):
    tesoro, coordenada = record 
    return coordenada
get_coordinate(("Scimshawed Whale Tooth", "2A"))

def convert_coordinate(coordinate):
    número, letra = coordinate 
    return número, letra
convert_coordinate(("2A"))


def create_record(azara_record, rui_record):
    tesoro, coordenada = azara_record
    ubicación, coordenada, cuadrante = rui_record
    if convert_coordinate(azara_record[1]) == convert_coordinate(rui_record[1]):
        return azara_record + rui_record
    else: 
        return "not a match"
create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))
