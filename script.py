import json
from collections import defaultdict, Counter

# ===== CONFIGURAÇÃO =====
CAMINHO_ARQUIVO = "1.json"  # ajuste para o nome do seu arquivo

# ===== LEITURA DO JSON =====
with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
    dados = json.load(f)

# ===== COLETAS =====
ids = []
respostas_map = defaultdict(list)

for item in dados:
    item_id = item.get("id")
    resposta_normalizada = item.get("resposta", "").strip().upper()

    ids.append(item_id)
    respostas_map[resposta_normalizada].append(item_id)

# ===== IDS DUPLICADOS =====
ids_contagem = Counter(ids)
ids_repetidos = [i for i, c in ids_contagem.items() if c > 1]

# ===== RESPOSTAS DUPLICADAS COM IDS =====
respostas_repetidas = {
    resposta: lista_ids
    for resposta, lista_ids in respostas_map.items()
    if len(lista_ids) > 1
}

# ===== IDS FALTANDO NA SEQUÊNCIA =====
ids_ordenados = sorted(ids)
ids_esperados = set(range(min(ids_ordenados), max(ids_ordenados) + 1))
ids_faltando = sorted(ids_esperados - set(ids_ordenados))

# ===== RESULTADO =====
print(f"Total de registros: {len(dados)}")

print("\nIDs repetidos:")
print(ids_repetidos if ids_repetidos else "Nenhum")

print("\nRespostas repetidas com IDs:")
if respostas_repetidas:
    for resposta, lista_ids in respostas_repetidas.items():
        print(f"- {resposta}: IDs {lista_ids}")
else:
    print("Nenhuma")

print("\nIDs faltando na sequência:")
print(ids_faltando if ids_faltando else "Nenhum")
