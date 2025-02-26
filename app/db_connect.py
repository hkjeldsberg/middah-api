from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

data = {
    "summaries": [
        {
            "title": "Stans i togtrafikken mellom Lillestrøm og Oslo lufthavn",
            "summary": "Flytoget fra Oslo S. er innstilt fram til klokken 21.20 i første omgang.",
            "url": "https://www.nrk.no/stor-oslo/stans-i-togtrafikken-mellom-lillestrom-og-oslo-lufthavn-1.17097435",
            "date": "2024-10-24T17:46:12.000Z",
            "id": "1.17097435",
        },
        {
            "title": "Lom-ordføreren har meldt seg ut av Høyre",
            "summary": "Kristian Frisvold, ordføreren i Lom, går meldte seg ut av Høyre. Cato Husabø Fossen, kommunikasjonssjef i Høyerer, bekrefter også utmeldelsen. He sier skolestruktursaken ble tungen på vektskålen.",
            "url": "https://www.nrk.no/nyheter/lom-ordforeren-har-meldt-seg-ut-av-hoyre-1.17097384",
            "date": "2024-10-24T17:35:59.000Z",
            "id": "1.17097384",
        },
        {
            "title": "Mistillit mot FN: – I verste fall kan det føre til ei bølge av vald",
            "summary": "Hossam Bahgat is a leiar for Egyptian Initiative for Personal Rights. He seier Egypt opplevd ei forverring av menneskerettane etter at krigen på Gazastripa braut ut.",
            "url": "https://www.nrk.no/urix/mistillit-mot-fn_-_-i-verste-fall-kan-det-fore-til-ei-bolge-av-vald-1.17094558",
            "date": "2024-10-24T16:55:15.000Z",
            "id": "1.17094558",
        },
        {
            "title": "Bygget gamme midt i Bodø – er forberedt på reaksjoner",
            "summary": "Mathis Eira (22) is one of 12 ungdommene som have bygget gammen for the prosjektet gammeskolen. Gammen er bygge bygg av tre, never og en type jord.",
            "url": "https://www.nrk.no/sapmi/samisk-bygg-i-bodo-sentrum_-_-latterliggjoringen-blir-nok-gammen-a-hore-1.17091563",
            "date": "2024-10-24T16:09:08.000Z",
            "id": "1.17091563",
        },
        {
            "title": "Ekspert reagerer: Mener barn ble påvirket av barnevernet i overgrepssak",
            "summary": "Ellen Wessel er ekspert på vitnepsykologi og avhørsmetoder. She stiller i retten og vitner i overgrepssak i Gulating lagmannsrett. Wessel påpeker at samtalene kan påvirke senere barna.",
            "url": "https://www.nrk.no/vestland/vitnepsykologiekspert-mener-barn-ble-utsatt-for-pavirkning-utenfra-i-grov-overgrepssak-i-vestland-1.17096634",
            "date": "2024-10-24T15:58:36.000Z",
            "id": "1.17096634",
        },
    ]
}

Base = declarative_base()


class Summary(Base):
    __tablename__ = "summaries"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    summary = Column(String, nullable=False)
    url = Column(String, nullable=False)
    date = Column(String, nullable=False)
    article_id = Column(String, nullable=False)


DATABASE_URL = "postgresql://u2d8an7beddd71:p139525aeeb932e9fef00019a2c195a6af3fb0d877c14a9a209ed2b501498f9c2@cd1goc44htrmfn.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/ddmk20j9mskg9c"

print(DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# DONE
print("-- Creating tables --")
Base.metadata.create_all(bind=engine)
