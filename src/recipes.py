import markdown.extensions.fenced_code
import pandas as pd
import random as rd

def restrict(df, *args):
    '''
    This function applies your food restrictions and returns a filtered df,
    based on up to the 5 restrictions that are created: dairy, gluten, nuts, vegan, vegetarian.
    It is done this way at it is significantly faster than iterating over the ingredients list and manual lists.
    '''
    if len(args)==0:
        return df
    elif len(args)==1:
        return df[~df[ args[0] ]].reset_index(drop=True)
    elif len(args)==2:
        return df[(~df[ args[0] ]) & (~df[ args[1] ])].reset_index(drop=True)
    elif len(args)==3:
        return df[(~df[ args[0] ]) & (~df[ args[1] ]) & (~df[ args[2] ])].reset_index(drop=True)
    elif len(args)==4:
        return df[(~df[ args[0] ]) & (~df[ args[1] ]) & (~df[ args[2] ]) & (~df[ args[3] ])].reset_index(drop=True)
    elif len(args)==5:
        return df[(~df[ args[0] ]) & (~df[ args[1] ]) & (~df[ args[2] ]) & (~df[ args[3] ]) & (~df[ args[4] ])].reset_index(drop=True)

def realfooder(df, ing_list, *args):
    '''
    This function selects your favourite ingredients and returns a filtered df by those ingredients only
    '''
    new_list=[i for ing in args for i in ing_list if ing in i]
    new_list = set(new_list)
    if new_list:
        ok=[]
        for index, row in df.iterrows():
            for i in row['ingredients']:
                if i in new_list:
                    ok.append(row.id)
                    break
        return df[df.id.isin(ok)].reset_index(drop=True)
    else:
        return f'There are no such ingredients in the ingredient list: {args}'

def picky_eater(df, ing_list, *args):
    '''
    This function excludes your loathed ingredients and returns a filtered df excluding those ingredients
    '''
    new_list=[i for ing in args for i in ing_list if ing in i]
    new_list = set(new_list)
    if new_list:
        yuck=[]
        for index, row in df.iterrows():
            for i in row['ingredients']:
                if i in new_list:
                    yuck.append(row.id)
                    break
        return df[~df.id.isin(yuck)].reset_index(drop=True)
    else: 
        return df

def n_of_recipes (n, k):
    '''
    This function recieves a total number of desired recipes and returns a random sample of indexes.
    These indexes will be used to determine the lucky df recipe indexes that are picked.
    '''

    if type(n)==int and type(k)==int and n>0 and k>0:
        if k<n:
            return rd.sample(range(n), k)
        else:
            print(f'There are only {n} recipes in this database')
            return range(n)
    else:
        return f'Nice try, now please provide a valid number between 1 and {n}'

def nutrition_values(nutrition):
    '''
    This function gives meaning to the nutrition values.
    '''
    # PDV stands for Percent Daily Value.
    # The percent Daily Value (%DV) shows how much a nutrient in a serving of food contributes to a total daily diet.
    nutrition[0] = f'calories(#): {nutrition[0]}'
    nutrition[1] = f'total fat (PDV): {nutrition[1]}'
    nutrition[2] = f'sugar (PDV): {nutrition[2]}'
    nutrition[3] = f'sodium (PDV): {nutrition[3]}'
    nutrition[4] = f'protein (PDV): {nutrition[4]}'
    nutrition[5] = f'saturated fat (PDV): {nutrition[5]}'
    nutrition[6] = f'carbohydrates (PDV): {nutrition[6]}'
    return nutrition