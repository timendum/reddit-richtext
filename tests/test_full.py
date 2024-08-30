from pprint import pprint

from rrichtext import RichTextContent


def test_parsing():
    # without formatting
    e = RichTextContent.parse_jobj(
        {
            "document": [
                {
                    "e": "par",
                    "c": [
                        {
                            "e": "text",
                            "t": "Piccola+analisi+di+questi+due+podcast+su+Youtube.",
                            "f": [[0, 0, 49]],
                        }
                    ],
                },
                {
                    "e": "par",
                    "c": [
                        {
                            "e": "text",
                            "t": "Se+vi+sono+piaciute+puntate+particolari,+segnalatele+nei+commenti.",
                            "f": [[0, 0, 66]],
                        }
                    ],
                },
                {
                    "e": "par",
                    "c": [
                        {
                            "e": "text",
                            "t": "Ho+visto+più+volte+citato+sia+Tintoria+che+Cachemire+qui+su+",
                            "f": [[0, 0, 59]],
                        },
                        {"e": "r/", "t": "italy", "l": False},
                        {
                            "e": "text",
                            "t": "+e+ho+provato+ad+avvicinarmi,+ma+soprattutto+Tintoria,+che+ha+più+di+200+puntate+lunghe+quasi+sempre+più+di+un'ora,+mi+è+sembrato+grosso+da+approcciare.",
                            "f": [[0, 1, 151]],
                        },
                    ],
                },
                {
                    "e": "par",
                    "c": [
                        {
                            "e": "text",
                            "t": "Quindi+ho+scaricato+da+Youtube+alcune+statistiche+delle+puntate+e+le+ho+rappresentate+su+un+grafico.",
                            "f": [[0, 0, 100]],
                        }
                    ],
                },
                {"e": "h", "l": 1, "c": [{"e": "raw", "t": "Tintoria"}]},
                {
                    "e": "img",
                    "id": "pfq19iv0mluc1",
                    "c": "Analisi+delle+puntate+di+Tintoria+Podcast",
                },
                {
                    "e": "par",
                    "c": [
                        {
                            "e": "text",
                            "t": "Ogni+pallino+rappresenta+una+puntata,+cioè+un+video+su+Youtube:+più+è+a+destra+più+è+recente,+più+è+in+alto+più+visualizzazioni+vengono+riportate,+più+è+giallo+e+più+Like+ha+in+rapporto+con+le+visualizzazioni+(giallo+vuol+dire+più+di+4+like+ogni+100+visualizzazioni).",
                            "f": [[0, 0, 267]],
                        }
                    ],
                },
                {
                    "e": "par",
                    "c": [
                        {
                            "e": "text",
                            "t": "Si+nota+un+boom+incredibile+a+fine+2023,+mi+sembra+a+seguito+dell'entrata+del+podcast+nel+circuito+OnePodcast+(di+Radio+Deejay);+altre+motivazioni+non+ne+ho+trovate.",
                            "f": [[0, 0, 165]],
                        }
                    ],
                },
                {
                    "e": "par",
                    "c": [
                        {
                            "e": "text",
                            "t": "Ho+trovato+fuori+norma+e+quindi+evidenzio:",
                            "f": [[0, 0, 42]],
                        }
                    ],
                },
                {
                    "e": "list",
                    "o": False,
                    "c": [
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Appello+a+Papa+Francesco",
                                            "u": "https://www.youtube.com/watch?v=AP260FbhNDk",
                                            "f": [[0, 0, 24]],
                                        },
                                        {
                                            "e": "text",
                                            "t": ",+che+ha+visualizzazioni+dieci+volte+tanto+rispetto+gli+altri+video+dello+stesso+periodo",
                                            "f": [[0, 0, 88]],
                                        },
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "text",
                                            "t": 'Discorso+simile+per+le+"Puntante+UGOS"++',
                                            "f": [[0, 0, 38]],
                                        },
                                        {
                                            "e": "link",
                                            "t": "1",
                                            "u": "https://www.youtube.com/watch?v=meQLFglZLoE",
                                            "f": [[0, 0, 1]],
                                        },
                                        {"e": "text", "t": ",+", "f": [[0, 0, 1]]},
                                        {
                                            "e": "link",
                                            "t": "2",
                                            "u": "https://www.youtube.com/watch?v=_w6xuUVniu4",
                                            "f": [[0, 0, 1]],
                                        },
                                        {"e": "text", "t": ",+", "f": [[0, 0, 1]]},
                                        {
                                            "e": "link",
                                            "t": "3",
                                            "u": "https://www.youtube.com/watch?v=https://www.youtube.com/watch?v=meQLFglZLoE",
                                            "f": [[0, 0, 1]],
                                        },
                                        {"e": "text", "t": ",+", "f": [[0, 0, 1]]},
                                        {
                                            "e": "link",
                                            "t": "4",
                                            "u": "https://www.youtube.com/watch?v=MLNoSsqIBhY",
                                            "f": [[0, 0, 1]],
                                        },
                                        {"e": "text", "t": ",+", "f": [[0, 0, 1]]},
                                        {
                                            "e": "link",
                                            "t": "5",
                                            "u": "https://www.youtube.com/watch?v=youkHSQ-qEU",
                                            "f": [[0, 0, 1]],
                                        },
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "text",
                                            "t": 'Un+rating+incredibilmente+alto+per+le+puntante+"In+tempo+di+quarantena",+quasi+tutte+sopra+i+4+Like+per+ogni+100+Views+(ma+hanno+meno+di+1,000+views+tipicamente).',
                                            "f": [[0, 0, 162]],
                                        }
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Stereotipi+sugli+ITALIANI",
                                            "u": "https://www.youtube.com/watch?v=wwZiaf03jd4",
                                            "f": [[0, 0, 25]],
                                        },
                                        {
                                            "e": "text",
                                            "t": ",+che+oltre+alle+Views+ha+anche+un+buon+rapporto+Like/Views",
                                            "f": [[0, 0, 59]],
                                        },
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Luca+Ravenna",
                                            "u": "https://youtube.com/watch?v=BJkFC-Efzcw",
                                            "f": [[0, 0, 12]],
                                        },
                                        {
                                            "e": "text",
                                            "t": "+è+la+seconda+a+superare+le+250,000+visualizzazioni",
                                            "f": [[0, 1, 50]],
                                        },
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "vs+Cachemire+Podcast",
                                            "u": "https://www.youtube.com/watch?v=PKYcoBmoYq4",
                                            "f": [[0, 0, 20]],
                                        },
                                        {
                                            "e": "text",
                                            "t": "+è+una+puntata+da+record,+la+prima+sopra+le+450,000",
                                            "f": [[0, 1, 50]],
                                        },
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "text",
                                            "t": "Altro+record+di+like+per++",
                                            "f": [[0, 0, 24]],
                                        },
                                        {
                                            "e": "link",
                                            "t": "Covid-19",
                                            "u": "https://www.youtube.com/watch?v=vpLKZ4RRtYc",
                                            "f": [[0, 0, 8]],
                                        },
                                        {
                                            "e": "text",
                                            "t": ",++46+Like+ogni+1000+Views,+e+siamo+oltre+le+10.000+visualizzazioni",
                                            "f": [[0, 0, 67]],
                                        },
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "text",
                                            "t": "Poi+ci+sono+tutte+quelle+TOP,+in+ordine",
                                            "f": [[0, 0, 39]],
                                        }
                                    ],
                                },
                                {
                                    "e": "list",
                                    "o": False,
                                    "c": [
                                        {
                                            "e": "li",
                                            "c": [
                                                {
                                                    "e": "par",
                                                    "c": [
                                                        {
                                                            "e": "link",
                                                            "t": "Pietro+Sermonti",
                                                            "u": "https://www.youtube.com/watch?v=L1Uuv0Gr2k8",
                                                            "f": [[0, 0, 15]],
                                                        }
                                                    ],
                                                }
                                            ],
                                        },
                                        {
                                            "e": "li",
                                            "c": [
                                                {
                                                    "e": "par",
                                                    "c": [
                                                        {
                                                            "e": "link",
                                                            "t": "Rocco+Tanica",
                                                            "u": "https://www.youtube.com/watch?v=4Slailmgku4",
                                                            "f": [[0, 0, 12]],
                                                        }
                                                    ],
                                                }
                                            ],
                                        },
                                        {
                                            "e": "li",
                                            "c": [
                                                {
                                                    "e": "par",
                                                    "c": [
                                                        {
                                                            "e": "link",
                                                            "t": "Frank+Matano",
                                                            "u": "https://www.youtube.com/watch?v=LjL1LuT7nRg",
                                                            "f": [[0, 0, 12]],
                                                        }
                                                    ],
                                                }
                                            ],
                                        },
                                        {
                                            "e": "li",
                                            "c": [
                                                {
                                                    "e": "par",
                                                    "c": [
                                                        {
                                                            "e": "link",
                                                            "t": "Maurizio+Battista",
                                                            "u": "https://www.youtube.com/watch?v=jMk1o9wYTNo",
                                                            "f": [[0, 0, 17]],
                                                        }
                                                    ],
                                                }
                                            ],
                                        },
                                        {
                                            "e": "li",
                                            "c": [
                                                {
                                                    "e": "par",
                                                    "c": [
                                                        {
                                                            "e": "link",
                                                            "t": "Alberto+Grandi",
                                                            "u": "https://www.youtube.com/watch?v=3z2cS1h_pYU",
                                                            "f": [[0, 0, 14]],
                                                        }
                                                    ],
                                                }
                                            ],
                                        },
                                        {
                                            "e": "li",
                                            "c": [
                                                {
                                                    "e": "par",
                                                    "c": [
                                                        {
                                                            "e": "link",
                                                            "t": "Lillo",
                                                            "u": "https://www.youtube.com/watch?v=UvVMjXGhpaQa",
                                                            "f": [[0, 0, 5]],
                                                        }
                                                    ],
                                                }
                                            ],
                                        },
                                        {
                                            "e": "li",
                                            "c": [
                                                {
                                                    "e": "par",
                                                    "c": [
                                                        {
                                                            "e": "link",
                                                            "t": "Valerio+Lundini",
                                                            "u": "https://www.youtube.com/watch?v=TYH6NrXXlEM&themeRefresh=1",
                                                            "f": [[0, 0, 15]],
                                                        }
                                                    ],
                                                }
                                            ],
                                        },
                                        {
                                            "e": "li",
                                            "c": [
                                                {
                                                    "e": "par",
                                                    "c": [
                                                        {
                                                            "e": "link",
                                                            "t": "Massimo+Ceccherini",
                                                            "u": "https://www.youtube.com/watch?v=1pBszVt2PRw",
                                                            "f": [[0, 0, 18]],
                                                        }
                                                    ],
                                                }
                                            ],
                                        },
                                    ],
                                },
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {"e": "text", "t": "Infine+segnalo+", "f": [[0, 0, 14]]},
                                        {
                                            "e": "link",
                                            "t": "Giancarlo+Magalli",
                                            "u": "https://www.youtube.com/watch?v=3-Fmp4xvBxc",
                                            "f": [[0, 0, 17]],
                                        },
                                        {
                                            "e": "text",
                                            "t": ",+che+ha+molte+views+e+un+buon+rapporto+Like/Views",
                                            "f": [[0, 0, 50]],
                                        },
                                    ],
                                }
                            ],
                        },
                    ],
                },
                {"e": "h", "l": 1, "c": [{"e": "raw", "t": "Cachemire"}]},
                {
                    "e": "par",
                    "c": [
                        {
                            "e": "text",
                            "t": "Stessa+cosa+anche+per+Cachemire+Podcast,+anche+se+ha+molte+meno+puntante:",
                            "f": [[0, 0, 73]],
                        }
                    ],
                },
                {
                    "e": "img",
                    "id": "byhskpvsrluc1",
                    "c": "Analisi+delle+puntate+di+Cachemire+Podcast",
                },
                {
                    "e": "par",
                    "c": [
                        {
                            "e": "text",
                            "t": "Qui+come+si+vede+le+puntate+sono+quasi+tutte+in+una+fascia+ben+definita,+tra+le+300,000+e+le+100,000+visualizzazioni.",
                            "f": [[0, 0, 117]],
                        }
                    ],
                },
                {"e": "par", "c": [{"e": "text", "t": "Segnalo+le+più+viste:", "f": [[0, 0, 21]]}]},
                {
                    "e": "list",
                    "o": False,
                    "c": [
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Damiano+David",
                                            "u": "https://www.youtube.com/watch?v=x8uyDNJGzFg",
                                            "f": [[0, 0, 13]],
                                        },
                                        {
                                            "e": "text",
                                            "t": ",+la+puntata+più+vista",
                                            "f": [[0, 0, 22]],
                                        },
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Frank+Matano",
                                            "u": "https://www.youtube.com/watch?v=J6wbsKlOUoo",
                                            "f": [[0, 0, 12]],
                                        },
                                        {
                                            "e": "text",
                                            "t": ",+ospite+molto+visto+anche+su+questo+podcast",
                                            "f": [[0, 0, 44]],
                                        },
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Valerio+Lundini",
                                            "u": "https://www.youtube.com/watch?v=prouISP730Y",
                                            "f": [[0, 0, 15]],
                                        },
                                        {"e": "text", "t": ",+seconda+costante", "f": [[0, 0, 18]]},
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Tutto+il+Belpaese+regione+per+regione",
                                            "u": "https://www.youtube.com/watch?v=7HckjtgN03g",
                                            "f": [[0, 0, 37]],
                                        },
                                        {
                                            "e": "text",
                                            "t": ",+la+puntata+più+vista+senza+ospite",
                                            "f": [[0, 0, 35]],
                                        },
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "La+puntata+crossover",
                                            "u": "https://www.youtube.com/watch?v=3HITTjqC69M",
                                            "f": [[0, 0, 20]],
                                        },
                                        {
                                            "e": "text",
                                            "t": ",+con+Rapone+e+Tinti",
                                            "f": [[0, 0, 20]],
                                        },
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Emanuela+Fanelli",
                                            "u": "https://www.youtube.com/watch?v=iOYdND7HlGE",
                                            "f": [[0, 0, 16]],
                                        }
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Roberto+Saviano",
                                            "u": "https://www.youtube.com/watch?v=_z8yI0JfjK0",
                                            "f": [[0, 0, 15]],
                                        }
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Caterina+Guzzanti",
                                            "u": "https://www.youtube.com/watch?v=vPAQH8me14Q",
                                            "f": [[0, 0, 17]],
                                        }
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Zerocalcare",
                                            "u": "https://www.youtube.com/watch?v=twBOBISCgXw",
                                            "f": [[0, 0, 11]],
                                        }
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Father&son",
                                            "u": "https://www.youtube.com/watch?v=SxyTlVHxBrc",
                                            "f": [[0, 0, 10]],
                                        },
                                        {
                                            "e": "text",
                                            "t": ",+la+puntata+con+i+genitori+di+Ferrario+e+Ravenna",
                                            "f": [[0, 0, 49]],
                                        },
                                    ],
                                }
                            ],
                        },
                    ],
                },
                {
                    "e": "par",
                    "c": [
                        {
                            "e": "text",
                            "t": "Inoltre,+eccezionali+per+il+rapporto+Like/Views:",
                            "f": [[0, 0, 48]],
                        }
                    ],
                },
                {
                    "e": "list",
                    "o": False,
                    "c": [
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Dario+Moccia",
                                            "u": "https://www.youtube.com/watch?v=ZOP991ANGd4",
                                            "f": [[0, 0, 12]],
                                        }
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {
                                            "e": "link",
                                            "t": "Il+Tempo+di+Una+Birra+parte+2",
                                            "u": "https://www.youtube.com/watch?v=QmQp-3XtVJg",
                                            "f": [[0, 0, 29]],
                                        }
                                    ],
                                }
                            ],
                        },
                        {
                            "e": "li",
                            "c": [
                                {
                                    "e": "par",
                                    "c": [
                                        {"e": "text", "t": "la+puntata+con+", "f": [[0, 0, 14]]},
                                        {
                                            "e": "link",
                                            "t": "Muschio+selvaggio",
                                            "u": "https://www.youtube.com/watch?v=zjixqVs0UUY",
                                            "f": [[0, 0, 17]],
                                        },
                                    ],
                                }
                            ],
                        },
                    ],
                },
                {
                    "e": "par",
                    "c": [
                        {
                            "e": "text",
                            "t": "Per+i+più+curiosi,+trovate+il+codice+usato+per+l'analisi+su+",
                            "f": [[0, 0, 59]],
                        },
                        {
                            "e": "link",
                            "t": "questo+gist",
                            "u": "https://gist.github.com/timendum/7a18176246d4c7466043484691c81359",
                            "f": [[0, 0, 11]],
                        },
                        {"e": "text", "t": ".", "f": [[0, 0, 1]]},
                    ],
                },
            ]
        }
    )
    pprint(e)

test_parsing()