from migrations.vagas import vagasData
from db.database import vagas_collection

for vaga in vagasData:
    result = vagas_collection.update_one(
        {"id": vaga["id"]}, {"$setOnInsert": vaga}, upsert=True
    )
    if result.upserted_id:
        print(f"✅ Inserida nova vaga: {vaga['title']}")
    else:
        print(f"⚠️ Vaga já existia: {vaga['title']}")
print("Migração de vagas concluída.")
