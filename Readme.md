# Recommendation service

```
[Пользователь] 
      │ (клик / оценка 1..5)
      ▼
[API Gateway / Service] ──(Event: UserRatedMovie)──▶ [ Apache Kafka ]
                                                            │
                     ┌──────────────────────────────────────┴──────────────────────────────────────┐
                     ▼                                                                             ▼
          [Real-Time Consumer]                                                           [Batch Storage / S3]
  * Обновляет онлайн-профиль в Redis                                                * Накопление обучающей выборки
  * Достает вектор юзера $u_i$                                                     * Периодический retrain модели
  * Считает Cosine Similarity / FAISS индекс                                        в PyTorch
  * Выдает Top-N в real-time
```