@echo off

set count=%1
echo Running %count% instances

FOR /L %%A IN (1,1,%count%) DO (
  start "" python src/main/python/kafka-producer.py --producer-name producer_%%A
)

echo Done