attrib_dict = {
    'POI name': 'name',
    'POI ID': 'id',
    'POI SysID': 'sys_id',
    'Link': 'url',
    'Format': 'format',
    'Tag': 'tag',
    'Length': 'len',
    'MW': 'mw',
    'pI': 'iso_point',
    'A0.1% (Ox)': 'extinction_ox',
    'A0.1% (Red)': 'extinction_red',
    'Concentration': 'concentration',
    'Description': 'description',
    'Stock ID': 'id',
    'Stock name': 'name',
    'Stock volume': 'volume',
    'Stock mass': 'weight',
    'Box ID': 'storage_id',
    'Box name': 'box',
    'Position': 'position',
    'Description': 'description',
    'Purification method': 'purification_method',
    'Storage buffer': 'storage buffer',
    'Source': 'species',
    'Sequence': 'sequence',
    'UniProt ID': 'web_page',
}

aa_dict = {
    'A': ('Ala', 'Alanine', 71.0788), 
    'R': ('Arg', 'Arginine', 156.1875), 
    'N': ('Asn', 'Asparagine', 114.1038), 
    'D': ('Asp', 'Aspartic Acid', 115.0886), 
    'C': ('Cys', 'Cysteine', 103.1388), 
    'Q': ('Gln', 'Glutamine', 128.1307), 
    'E': ('Glu', 'Glutamic Acid', 129.1155), 
    'G': ('Gly', 'Glycine', 57.0519), 
    'H': ('His', 'Histidine', 137.1411), 
    'I': ('Ile', 'Isoleucine', 113.1594), 
    'L': ('Leu', 'Leucine', 113.1594), 
    'K': ('Lys', 'Lysine', 128.1741), 
    'M': ('Met', 'Methionine', 131.1926), 
    'F': ('Phe', 'Phenylalanine', 147.1766), 
    'P': ('Pro', 'Proline', 97.1167), 
    'S': ('Ser', 'Serine', 87.0782), 
    'T': ('Thr', 'Threonine', 101.1051), 
    'W': ('Trp', 'Tryptophan', 186.2132), 
    'Y': ('Tyr', 'Tyrosine', 163.176), 
    'V': ('Val', 'Valine', 99.1326)
    }

prot_attribs = ["ws_name",
                "name",
                "id",
                "sys_id",
                "owner_id",
                "alternative_name",
                "gene",
                "species",
                "mutations",
                "chemical_modifications",
                "purification_method",
                "mw",
                "iso_point",
                "extinction_ox",
                "extinction_red",
                "storage_buffer",
                "storage_temperature",
                "sequence",
                "web_page",
                "description",
                "tag",
                ]
