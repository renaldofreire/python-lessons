distancia_km = 10
distancia_mi = distancia_km * 0.62

t_minuto = 42
t_segundo = 42
t_hora = t_minuto / 60 + t_segundo / 3600

r_medio_hora = t_hora / distancia_mi
r_medio_minuto = r_medio_hora * 60
r_medio_segundo = (r_medio_minuto - int(r_medio_minuto)) * 60

vel_media = distancia_mi / t_hora

print(
    f"Ritmo médio: {int(r_medio_minuto)} minutos e {int(r_medio_segundo)} segundos por milha"
)
