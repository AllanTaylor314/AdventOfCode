from math import ceil

class NanoFactory:
    def __init__(self, recipe_dict):
        self.ore_used=0
        self.stockpile={'ORE':0}
        self.recipe_dict=recipe_dict
    def generate(self,name,count=1):
        if name=='ORE':
            self.stockpile['ORE']+=count
            self.ore_used+=count
            if self.ore_used>1e12:
                print('Part 2:',self.stockpile.get('FUEL',0))
                quit()
            return
        if name not in self.stockpile:
            self.stockpile[name]=0
        quantity,ingredients=self.recipe_dict[name]
        multiplier=ceil(count/quantity)
        # Generate all of the required materials
        for ing,q in ingredients:
            # Generate the shortfall
            self.generate(ing,q*multiplier-self.stockpile.get(ing,0))
            # Remove what we used
            self.stockpile[ing]-=q*multiplier
        # Add what we just created
        self.stockpile[name]+=quantity*multiplier

with open('14.txt') as file:
    recipes = file.read().splitlines()

def resource_count(rec_str):
    count,name=rec_str.split()
    return name,int(count)

def process_recipe(recipe):
    ingredient_str,product_str=recipe.split(' => ')
    product=resource_count(product_str)
    ingredient_list=[resource_count(_) for _ in ingredient_str.split(', ')]
    return ingredient_list, product

recipe_dict = {p[0]:(p[1],i) for i,p in (process_recipe(_) for _ in recipes)}
nanofactory = NanoFactory(recipe_dict)
nanofactory.generate('FUEL')
max_ore_per_fuel=nanofactory.ore_used
print('Part 1:',max_ore_per_fuel,flush=True)

# Generate as much FUEL as we can with the resources available, until there
# is not enough ORE to make a FUEL from scratch
while (int(1e12)-nanofactory.ore_used)>max_ore_per_fuel:
    nanofactory.generate('FUEL',(int(1e12)-nanofactory.ore_used)//max_ore_per_fuel)
# Generate FUEL with whatever is left (nanofactory will quit once out of ORE)
while True:
    nanofactory.generate('FUEL')
