number = int(input())
total_heroes = {}

for _ in range(number):
    hero_name, hp, mp = input().split()
    total_heroes[hero_name] = [int(hp), int(mp)]

command = input().split(' - ')

while command[0] != 'End':

    if command[0] == 'CastSpell':
        hero_name, mp_needed, spell_name = command[1], int(command[2]), command[3]
        hero_mp = total_heroes[hero_name][1]
        if hero_mp >= mp_needed:
            total_heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {total_heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command[0] == 'TakeDamage':
        hero_name, damage, attacker = command[1], int(command[2]), command[3]
        total_heroes[hero_name][0] -= damage
        if total_heroes[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {total_heroes[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            total_heroes.pop(hero_name)

    elif command[0] == 'Recharge':
        hero_name, amount = command[1], int(command[2])
        hero_mp = total_heroes[hero_name][1]
        recovery = min(hero_mp + amount, 200)
        total_heroes[hero_name][1] = recovery
        total_recovered = recovery - hero_mp
        print(f"{hero_name} recharged for {total_recovered} MP!")

    elif command[0] == 'Heal':
        hero_name, amount = command[1], int(command[2])
        hero_hp = total_heroes[hero_name][0]
        healing = min(hero_hp + amount, 100)
        total_heroes[hero_name][0] = healing
        healed = healing - hero_hp
        print(f"{hero_name} healed for {healed} HP!")

    command = input().split(' - ')

for hero, stats in total_heroes.items():
    print(f'{hero}')
    print(f'  HP: {stats[0]}')
    print(f'  MP: {stats[1]}')