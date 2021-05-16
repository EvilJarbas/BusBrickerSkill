# BusBrickerSkill
this skill will shudown the messagebus for all other skills

## LOGS

```
2021-05-16 02:36:56.229 | WARNING  | 304406 | BusBrickerSkill | All skills share a messagebus object, this means any skill can call the shutdown method and brick your mycroft
2021-05-16 02:36:56.230 | WARNING  | 304406 | BusBrickerSkill | DO NOT INSTALL RANDOM CRAP
2021-05-16 02:36:56.230 | ERROR    | 304406 | BusBrickerSkill | each skill should have it's own bus instance
2021-05-16 02:36:56.230 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.231 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.236 | INFO     | 304406 | mycroft.skills.skill_loader:load:185 | ATTEMPTING TO LOAD SKILL: skill-picfixer
2021-05-16 02:36:56.238 | INFO     | 304406 | mycroft.skills.settings:get_local_settings:83 | /home/user/.config/mycroft/skills/skill-picfixer/settings.json
2021-05-16 02:36:56.245 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.245 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.246 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.246 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.248 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.248 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.248 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.249 | INFO     | 304406 | mycroft.skills.skill_loader:_communicate_load_status:344 | Skill skill-picfixer loaded successfully
2021-05-16 02:36:56.249 | INFO     | 304406 | mycroft.skills.skill_loader:load:185 | ATTEMPTING TO LOAD SKILL: skill-omeleto
2021-05-16 02:36:56.252 | INFO     | 304406 | mycroft.skills.settings:get_local_settings:83 | /home/user/.config/mycroft/skills/skill-omeleto/settings.json
2021-05-16 02:36:56.259 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.259 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.260 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.260 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.260 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.260 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.260 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.261 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown
2021-05-16 02:36:56.261 | ERROR    | 304406 | websocket | error from callback <bound method MessageBusClient.on_message of <mycroft.messagebus.client.client.MessageBusClient object at 0x7feb895b6a60>>: cannot schedule new futures after shutdown

```

## Patch

see https://github.com/HelloChatterbox/HolmesV/pull/37
