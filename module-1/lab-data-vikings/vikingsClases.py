
# Soldier
import random


class Soldier:
	def __init__(self, health, strength):
		self.health = health
		self.strength = strength

	def attack(self):
		return self.strength

	def receiveDamage(self, damage):
		self.health = self.health - damage

	pass

# Viking

	
class Viking(Soldier):
	def __init__(self, name, health, strength):
		super().__init__(health,strength)
		self.name = name

	def receiveDamage(self, damage):
		self.health = self.health - damage
		if self.health > 0:
			return self.name+' has received '+str(damage)+' points of damage'
		elif self.health <= 0:
			return self.name+' has died in act of combat'

	def battleCry(self):
		return 'Odin Owns You All!'

	pass

# Saxon


class Saxon(Soldier):
	def __init__(self,health,strength):
		super().__init__(health, strength)

	def attack(self):
		return self.strength

	def receiveDamage(self, damage):
		self.health = self.health - damage
		if self.health > 0:
			return 'A Saxon has received '+str(damage)+' points of damage'
		elif self.health <= 0:
			return 'A Saxon has died in combat'

	pass

# War


class War:
	def __init__(self):
		self.vikingArmy = []
		self.saxonArmy = []

	def addViking(self, Viking):
		self.vikingArmy.append(Viking)

	def addSaxon(self, Saxon):
		self.saxonArmy.append(Saxon)

	def vikingAttack(self):
		r_vik = random.choice(self.vikingArmy)
		r_sax = random.choice(self.saxonArmy)

		#Voy a mandar llamar la función attack de un Viking.
		sax_dam = r_sax.receiveDamage(r_vik.attack())

		if r_sax.health <= 0:
			self.saxonArmy.remove(r_sax)

		return sax_dam
	pass

	def saxonAttack(self):
		r_vik = random.choice(self.vikingArmy)
		r_sax = random.choice(self.saxonArmy)
		vik_dam = r_vik.receiveDamage(r_sax.attack())
		
		if r_vik.health <=0:
			self.vikingArmy.remove(r_vik)
		return vik_dam

	def showStatus(self):
		if len(self.saxonArmy) == 0:
			return 'Vikings have won the war of the century!'
		elif len(self.vikingArmy) == 0:
			return 'Saxons have fought for their lives and survive another day...'
		elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
			return 'Vikings and Saxons are still in the thick of battle.'