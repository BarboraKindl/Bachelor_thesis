import re
import pandas as pd


def clean_rem_epileptiformni_aktivita(aktivita):
    if pd.isna(aktivita):
        return aktivita
    aktivita = aktivita.lower().strip()

    categories = []

    if any(word in aktivita for word in
           ['žádná', 'none', 'ne', 'neuvedena', 'nebyla zaznamenána',
            'nepřítomnost']):
        categories.append('žádná epileptiformní aktivita')
    if any(word in aktivita for word in ['spike', 'hrot', 'hroty']):
        categories.append('spike/hroty')
    if any(word in aktivita for word in ['sharp', 'ostré']):
        categories.append('ostré vlny')
    if any(word in aktivita for word in ['sw complex', 'spike-wave']):
        categories.append('spike-wave komplexy')
    if any(word in aktivita for word in ['polymorphic', 'polymorfní']):
        categories.append('polymorfní aktivita')
    if any(word in aktivita for word in ['generalizovaná', 'generalized']):
        categories.append('generalizovaná aktivita')
    if any(word in aktivita for word in ['focal', 'fokální']):
        categories.append('fokální aktivita')
    if any(word in aktivita for word in ['paroxysmální', 'paroxysmal']):
        categories.append('paroxysmální aktivita')
    if any(word in aktivita for word in ['epileptiformní', 'epileptiform']):
        categories.append('epileptiformní aktivita')
    if any(word in aktivita for word in ['hypsarrytmie', 'hypsarrhythmia']):
        categories.append('hypsarrytmie')
    if any(word in aktivita for word in ['sínusový rytmus', 'sinus rhythm']):
        categories.append('sínusový rytmus')
    if any(word in aktivita for word in ['delta', 'delta waves']):
        categories.append('delta vlny')
    if any(word in aktivita for word in ['theta', 'theta waves']):
        categories.append('theta vlny')
    if any(word in aktivita for word in ['beta', 'beta waves']):
        categories.append('beta vlny')
    if any(word in aktivita for word in ['gamma', 'gamma waves']):
        categories.append('gamma vlny')

    electrodes = []
    possible_electrodes = ['fz', 'f9', 'f8', 'f7', 'f4', 'f3', 'fp2', 'fp1',
                           't3', 't4', 't5', 't6', 'p3', 'p4', 'p10', 'o1',
                           'o2', 'c4', 'c3', 'pz', 'cz']
    for electrode in possible_electrodes:
        if electrode in aktivita:
            electrodes.append(electrode.upper())

    if electrodes:
        categories.append('elektrody: ' + ', '.join(electrodes))

    if not categories:
        categories.append('ostatní: ' + aktivita)

    return ', '.join(categories)


def clean_arealni_diferenciace(diferenciace):
    if pd.isna(diferenciace):
        return diferenciace
    diferenciace = diferenciace.lower().strip()

    categories = []

    if any(word in diferenciace for word in ['žádná', 'none']):
        categories.append('žádná diferenciace')
    if any(word in diferenciace for word in ['vlevo', 'left']):
        categories.append('diferenciace vlevo')
    if any(word in diferenciace for word in ['vpravo', 'right']):
        categories.append('diferenciace vpravo')
    if any(word in diferenciace for word in ['bilaterální', 'bilateral']):
        categories.append('bilaterální diferenciace')
    if any(word in diferenciace for word in ['generalizovaná', 'generalized']):
        categories.append('generalizovaná diferenciace')
    if any(word in diferenciace for word in ['centrální', 'central']):
        categories.append('centrální diferenciace')

    if not categories:
        categories.append('ostatní: ' + diferenciace)

    return ', '.join(categories)


def clean_asymetrie_mu_rytmu(asymetrie):
    if pd.isna(asymetrie):
        return asymetrie
    asymetrie = asymetrie.lower().strip()

    categories = []

    if any(word in asymetrie for word in ['žádná', 'none', 'ne']):
        categories.append('žádná asymetrie')
    if any(word in asymetrie for word in ['levá', 'left']):
        categories.append('asymetrie na levé straně')
    if any(word in asymetrie for word in ['pravá', 'right']):
        categories.append('asymetrie na pravé straně')
    if any(word in asymetrie for word in ['bilaterální', 'bilateral']):
        categories.append('bilaterální asymetrie')
    if any(word in asymetrie for word in ['generalizovaná', 'generalized']):
        categories.append('generalizovaná asymetrie')
    if any(word in asymetrie for word in ['centrální', 'central']):
        categories.append('centrální asymetrie')
    if any(word in asymetrie for word in ['epileptiformní', 'epileptiform']):
        categories.append('epileptiformní asymetrie')
    if any(word in asymetrie for word in ['přední', 'anterior']):
        categories.append('přední asymetrie')
    if any(word in asymetrie for word in ['zadní', 'posterior']):
        categories.append('zadní asymetrie')
    if any(word in asymetrie for word in ['horní', 'superior']):
        categories.append('horní asymetrie')
    if any(word in asymetrie for word in ['dolní', 'inferior']):
        categories.append('dolní asymetrie')

    if not categories:
        categories.append('ostatní: ' + asymetrie)

    return ', '.join(categories)


def clean_fctp_oblast_zpomaleni(oblast):
    if pd.isna(oblast):
        return oblast
    oblast = oblast.lower().strip()

    categories = []

    if any(word in oblast for word in ['frontální', 'frontal']):
        categories.append('frontální oblast')
    if any(word in oblast for word in ['centrální', 'central']):
        categories.append('centrální oblast')
    if any(word in oblast for word in ['temporální', 'temporal']):
        categories.append('temporální oblast')
    if any(word in oblast for word in ['parietální', 'parietal']):
        categories.append('parietální oblast')
    if any(word in oblast for word in ['okcipitální', 'occipital']):
        categories.append('okcipitální oblast')
    if any(word in oblast for word in ['levá', 'left']):
        categories.append('levá strana')
    if any(word in oblast for word in ['pravá', 'right']):
        categories.append('pravá strana')
    if any(word in oblast for word in ['bilaterální', 'bilateral']):
        categories.append('bilaterální oblast')
    if any(word in oblast for word in ['generalizovaná', 'generalized']):
        categories.append('generalizovaná oblast')
    if any(word in oblast for word in ['anterior']):
        categories.append('přední oblast')
    if any(word in oblast for word in ['posterior']):
        categories.append('zadní oblast')
    if any(word in oblast for word in ['superior']):
        categories.append('horní oblast')
    if any(word in oblast for word in ['inferior']):
        categories.append('dolní oblast')

    if not categories:
        categories.append('ostatní: ' + oblast)

    return ', '.join(categories)


def clean_epileptiformni_aktivita(aktivita):
    if pd.isna(aktivita):
        return aktivita
    aktivita = aktivita.lower().strip()

    categories = []

    if any(word in aktivita for word in ['žádná', 'none', 'ne']):
        categories.append('žádná epileptiformní aktivita')
    if any(word in aktivita for word in
           ['přítomnost', 'ano', 'epileptiformní aktivita', 'patrná',
            'přítomná', 'true']):
        categories.append('přítomna')
    if any(word in aktivita for word in ['spike', 'hrot', 'hroty']):
        categories.append('spike/hroty')
    if any(word in aktivita for word in ['sharp', 'ostré']):
        categories.append('ostré vlny')
    if any(word in aktivita for word in ['sw complex', 'spike-wave']):
        categories.append('spike-wave komplexy')
    if any(word in aktivita for word in ['polymorphic', 'polymorfní']):
        categories.append('polymorfní aktivita')
    if any(word in aktivita for word in ['generalizovaná', 'generalized']):
        categories.append('generalizovaná aktivita')
    if any(word in aktivita for word in ['focal', 'fokální']):
        categories.append('fokální aktivita')
    if any(word in aktivita for word in ['paroxysmální', 'paroxysmal']):
        categories.append('paroxysmální aktivita')
    if any(word in aktivita for word in ['epileptiformní', 'epileptiform']):
        categories.append('epileptiformní aktivita')
    if any(word in aktivita for word in ['hypsarrytmie', 'hypsarrhythmia']):
        categories.append('hypsarrytmie')
    if any(word in aktivita for word in ['sínusový rytmus', 'sinus rhythm']):
        categories.append('sínusový rytmus')
    if any(word in aktivita for word in ['delta', 'delta waves']):
        categories.append('delta vlny')
    if any(word in aktivita for word in ['theta', 'theta waves']):
        categories.append('theta vlny')
    if any(word in aktivita for word in ['beta', 'beta waves']):
        categories.append('beta vlny')
    if any(word in aktivita for word in ['gamma', 'gamma waves']):
        categories.append('gamma vlny')

    if not categories:
        categories.append('ostatní: ')

    return ', '.join(categories)


def clean_maxima_epileptiformni_aktivity(aktivita):
    if pd.isna(aktivita):
        return aktivita
    aktivita = aktivita.lower().strip()

    categories = []

    if any(word in aktivita for word in ['žádná', 'none', 'ne']):
        categories.append('žádná maxima')
    if any(word in aktivita for word in ['frontální', 'frontal']):
        categories.append('frontální maxima')
    if any(word in aktivita for word in ['centrální', 'central']):
        categories.append('centrální maxima')
    if any(word in aktivita for word in ['temporální', 'temporal']):
        categories.append('temporální maxima')
    if any(word in aktivita for word in ['parietální', 'parietal']):
        categories.append('parietální maxima')
    if any(word in aktivita for word in ['okcipitální', 'occipital']):
        categories.append('okcipitální maxima')
    if any(word in aktivita for word in ['levá', 'left']):
        categories.append('maxima vlevo')
    if any(word in aktivita for word in ['pravá', 'right']):
        categories.append('maxima vpravo')
    if any(word in aktivita for word in ['bilaterální', 'bilateral']):
        categories.append('bilaterální maxima')
    if any(word in aktivita for word in ['generalizovaná', 'generalized']):
        categories.append('generalizovaná maxima')

    electrodes = []
    possible_electrodes = ['fz', 'f9', 'f8', 'f7', 'f4', 'f3', 'fp2', 'fp1',
                           't3', 't4', 't5', 't6', 'p3', 'p4', 'p10', 'o1',
                           'o2', 'c4', 'c3', 'pz', 'cz']
    for electrode in possible_electrodes:
        if electrode in aktivita:
            electrodes.append(electrode.upper())

    if electrodes:
        categories.append('elektrody: ' + ', '.join(electrodes))

    if not categories:
        categories.append('ostatní: ' + aktivita)

    return ', '.join(categories)


def clean_asymetrie_mu_rytmu(asymetrie):
    if pd.isna(asymetrie):
        return asymetrie
    asymetrie = asymetrie.lower().strip()

    categories = []

    if any(word in asymetrie for word in ['žádná', 'none']):
        categories.append('žádná asymetrie')
    if any(word in asymetrie for word in ['levá', 'left']):
        categories.append('asymetrie na levé straně')
    if any(word in asymetrie for word in ['pravá', 'right']):
        categories.append('asymetrie na pravé straně')
    if any(word in asymetrie for word in ['bilaterální', 'bilateral']):
        categories.append('bilaterální asymetrie')
    if any(word in asymetrie for word in ['generalizovaná', 'generalized']):
        categories.append('generalizovaná asymetrie')
    if any(word in asymetrie for word in ['centrální', 'central']):
        categories.append('centrální asymetrie')

    if not categories:
        categories.append('ostatní')

    ret = ', '.join(categories)
    if re.sub(r'\bostatní:\b', '', asymetrie):
        return None
    else:
        return ret


def clean_okcipitalni_rytm(rytmus):
    if pd.isna(rytmus):
        return rytmus
    rytmus = rytmus.lower().strip()

    if any(word in rytmus for word in
           ['žádná entita', 'žádný identifikován', 'neuvedeno']):
        return None

    categories = []

    if 'asymetrie MU rytmu' in rytmus:
        categories.append('asymetrie MU rytmu')
    if any(word in rytmus for word in ['alfa', 'alpha']):
        categories.append('alfa rytmus')
    if 'beta' in rytmus:
        categories.append('beta rytmus')
    if 'theta' in rytmus:
        categories.append('theta rytmus')
    if 'delta' in rytmus:
        categories.append('delta rytmus')
    if any(word in rytmus for word in ['pomalý', 'slow']):
        categories.append('pomalý rytmus')
    if any(word in rytmus for word in ['rychlý', 'fast']):
        categories.append('rychlý rytmus')
    if any(word in rytmus for word in ['normální', 'normal']):
        categories.append('normální rytmus')

    if not categories:
        categories.append('ostatní: ' + rytmus)

    return ', '.join(categories)


def clean_typy_eeg_aktivit(typ):
    if pd.isna(typ):
        return typ
    typ = typ.lower().strip()

    categories = []

    # Consolidation of terms
    if any(word in typ for word in ['rytm', 'ritm']):
        categories.append('rytmická aktivita')
    if any(word in typ for word in ['ostré vlny', 'sharp', 'sharp waves']):
        categories.append('ostré vlny')
    if any(word in typ for word in ['hroty', 'spike', 'spikes', 'hrot']):
        categories.append('hroty')
    if any(word in typ for word in
           ['sw komplexy', 'spike-wave', 'sw complex']):
        categories.append('sw komplexy')
    if any(word in typ for word in ['pomalé', 'slow', 'delta']):
        categories.append('pomalé vlny')
    if 'epileptiformní' in typ or 'epileptiform' in typ:
        categories.append('epileptiformní aktivity')
    if 'beta' in typ:
        categories.append('beta aktivita')
    if 'theta' in typ:
        categories.append('theta aktivita')
    if any(word in typ for word in ['alfa', 'alpha']):
        categories.append('alfa aktivita')
    if 'polymorfní' in typ:
        categories.append('polymorfní aktivita')
    if 'generalizované' in typ or 'generalizace' in typ:
        categories.append('generalizovaná aktivita')
    if 'fokální' in typ or 'focal' in typ:
        categories.append('fokální aktivita')
    if 'intermitentní' in typ:
        categories.append('intermitentní aktivita')
    if 'kontinuální' in typ or 'continuous' in typ:
        categories.append('kontinuální aktivita')
    if 'paroxysmální' in typ:
        categories.append('paroxysmální aktivita')
    if 'hypsarytmie' in typ:
        categories.append('hypsarytmie')
    if 'low voltage' in typ or 'nízkovoltážní' in typ:
        categories.append('nízkovoltážní aktivita')
    if 'high voltage' in typ or 'vysokovoltážní' in typ:
        categories.append('vysokovoltážní aktivita')
    if 'periodické' in typ or 'periodic' in typ:
        categories.append('periodické aktivity')

    if not categories:
        categories.append('ostatní')

    return ', '.join(categories)


def clean_lokalizace(lokalizace):
    if pd.isna(lokalizace):
        return lokalizace
    lokalizace = lokalizace.lower().strip()

    categories = []
    electrodes = []

    # Consolidation of terms
    if any(word in lokalizace for word in ['front', 'frontal']):
        categories.append('frontální lalok')
    if any(word in lokalizace for word in ['tempor', 'temporal']):
        categories.append('temporální lalok')
    if any(word in lokalizace for word in ['pariet', 'parietal']):
        categories.append('parietální lalok')
    if any(word in lokalizace for word in ['occipit', 'occipital']):
        categories.append('okcipitální lalok')
    if any(word in lokalizace for word in ['centr', 'central']):
        categories.append('centrální oblast')
    if 'lev' in lokalizace or 'left' in lokalizace:
        categories.append('levá strana')
    if 'prav' in lokalizace or 'right' in lokalizace:
        categories.append('pravá strana')
    if 'bilaterální' in lokalizace or 'bilateral' in lokalizace:
        categories.append('bilaterální')
    if 'generali' in lokalizace or 'general' in lokalizace:
        categories.append('generalizovaná')

    possible_electrodes = ['fz', 'f9', 'f8', 'f7', 'f4', 'f3', 'fp2', 'fp1',
                           't3', 't4', 't5', 't6', 'p3', 'p4', 'p10', 'o1',
                           'o2', 'c4', 'c3', 'pz', 'cz']
    for electrode in possible_electrodes:
        if electrode in lokalizace:
            electrodes.append(electrode.upper())

    if electrodes:
        categories.append('elektrody: ' + ', '.join(electrodes))

    if not categories:
        categories.append(lokalizace)

    return ', '.join(categories)


def clean_specifika(specifika):
    if pd.isna(specifika):
        return specifika
    specifika = specifika.lower().strip()

    categories = []
    electrodes = []

    if any(word in specifika for word in
           ['epileptogenní zóna', 'epileptogenic zone']):
        categories.append('epileptogenní zóna')
    if any(word in specifika for word in ['semiologicky', 'semiology']):
        categories.append('semiologické rysy')
    if any(word in specifika for word in ['nespecifická', 'nonspecific']):
        categories.append('nespecifické')
    if any(word in specifika for word in ['cefalgická aura', 'cephalic aura']):
        categories.append('cefalgická aura')
    if any(word in specifika for word in ['abnormální', 'abnormal']):
        categories.append('abnormální aktivity')
    if any(word in specifika for word in ['zpomalení', 'slowing']):
        categories.append('zpomalení')
    if any(word in specifika for word in ['rychlá', 'fast']):
        categories.append('rychlá aktivita')
    if any(word in specifika for word in ['kontinuální', 'continuous']):
        categories.append('kontinuální aktivita')
    if any(word in specifika for word in ['intermitentní', 'intermittent']):
        categories.append('intermitentní aktivita')
    if any(word in specifika for word in
           ['spánková aktivita', 'sleep activity']):
        categories.append('spánková aktivita')
    if any(word in specifika for word in ['bdění', 'wakefulness']):
        categories.append('aktivita během bdění')
    if any(word in specifika for word in ['frekvence', 'frequency']):
        categories.append('frekvenční změny')
    if any(word in specifika for word in
           ['epileptiformní výboje', 'epileptiform discharges']):
        categories.append('epileptiformní výboje')
    if any(word in specifika for word in ['generalizované', 'generalized']):
        categories.append('generalizované aktivity')

    possible_electrodes = ['fz', 'f9', 'f8', 'f7', 'f4', 'f3', 'fp2', 'fp1',
                           't3', 't4', 't5', 't6', 'p3', 'p4', 'p10', 'o1',
                           'o2', 'c4', 'c3', 'pz', 'cz']
    for electrode in possible_electrodes:
        if electrode in specifika:
            electrodes.append(electrode.upper())

    if electrodes:
        categories.append('elektrody: ' + ', '.join(electrodes))

    if not categories:
        categories.append("ostatní: " + specifika)

    return ', '.join(categories)


def clean_sleep_awake(aktivita):
    if pd.isna(aktivita):
        return aktivita
    aktivita = aktivita.lower().strip()

    if any(word in aktivita for word in ['neuvedeno']):
        return None

    categories = []

    if any(word in aktivita for word in
           ['spánek', 've spánku', 'ze spánku', 'sleep']):
        categories.append('spánek')
    if any(word in aktivita for word in ['bdění', 'wakefulness', 'awake']):
        categories.append('bdění')
    if 'rem' in aktivita:
        categories.append('REM spánek')
    if 'nrem' in aktivita or 'non-rem' in aktivita:
        categories.append('NREM spánek')
    if any(word in aktivita for word in ['hluboký spánek', 'deep sleep']):
        categories.append('hluboký spánek')
    if any(word in aktivita for word in ['lehky spánek', 'light sleep']):
        categories.append('lehký spánek')
    if any(word in aktivita for word in ['snící fáze', 'dream phase']):
        categories.append('snící fáze')
    if any(word in aktivita for word in
           ['hypnagogické stavy', 'hypnagogic states']):
        categories.append('hypnagogické stavy')

    if not categories:
        categories.append('ostatní: ' + aktivita)

    return ', '.join(categories)


def clean_lateralita(lateralita):
    if pd.isna(lateralita):
        return lateralita

    if any(word in lateralita for word in ['neuvedeno']):
        return None

    lateralita = lateralita.lower().strip()

    categories = []

    if any(word in lateralita for word in
           ['levá', 'vlevo', 'doleva', 'levé', 'levostranná', 'left']):
        categories.append('levá strana')
    if any(word in lateralita for word in
           ['pravá', 'vpravo', 'doprava', 'pravostranná', 'right']):
        categories.append('pravá strana')
    if any(word in lateralita for word in ['bilaterální', 'bilateral']):
        categories.append('bilaterální')
    if any(word in lateralita for word in ['generalizovaná', 'generalized']):
        categories.append('generalizovaná')
    if any(word in lateralita for word in ['hemisféra', 'hemisphere']):
        categories.append('hemisféra')
    if any(word in lateralita for word in ['centrální', 'central']):
        categories.append('centrální')
    if any(word in lateralita for word in ['ipsilaterální', 'ipsilateral']):
        categories.append('ipsilaterální')
    if any(word in lateralita for word in
           ['kontralaterální', 'contralateral']):
        categories.append('kontralaterální')
    if any(word in lateralita for word in ['přední', 'anterior']):
        categories.append('přední')
    if any(word in lateralita for word in ['zadní', 'posterior']):
        categories.append('zadní')
    if any(word in lateralita for word in ['horní', 'superior']):
        categories.append('horní')
    if any(word in lateralita for word in ['dolní', 'inferior']):
        categories.append('dolní')

    if not categories:
        categories.append('ostatní: ' + lateralita)

    return ', '.join(categories)


def clean_typ_aktivity(typ_aktivity):
    if pd.isna(typ_aktivity):
        return typ_aktivity

    if any(word in typ_aktivity for word in
           ['neuvedeno', 'žádný identifikován']):
        return None

    typ_aktivity = typ_aktivity.lower().strip()

    # Remove a specific expression
    typ_aktivity = typ_aktivity.replace('video/eeg monitorování', ' ')

    # Split the string into words, remove empty strings, and rejoin
    typ_aktivity = ' '.join(filter(None, typ_aktivity.split()))

    categories = []

    if any(word in typ_aktivity for word in ['spike', 'hrot', 'hroty']):
        categories.append('spike/hroty')
    if any(word in typ_aktivity for word in ['slow', 'pomalé', 'delta']):
        categories.append('pomalé vlny')
    if any(word in typ_aktivity for word in ['sharp', 'ostré']):
        categories.append('ostré vlny')
    if any(word in typ_aktivity for word in ['sw complex', 'spike-wave']):
        categories.append('spike-wave komplexy')
    if any(word in typ_aktivity for word in ['polymorphic', 'polymorfní']):
        categories.append('polymorfní aktivita')
    if any(word in typ_aktivity for word in ['beta']):
        categories.append('beta aktivita')
    if any(word in typ_aktivity for word in ['theta']):
        categories.append('theta aktivita')
    if any(word in typ_aktivity for word in ['alpha', 'alfa']):
        categories.append('alfa aktivita')
    if any(word in typ_aktivity for word in ['fast', 'rychlá']):
        categories.append('rychlá aktivita')
    if any(word in typ_aktivity for word in ['continuous', 'kontinuální']):
        categories.append('kontinuální aktivita')
    if any(word in typ_aktivity for word in ['intermittent', 'intermitentní']):
        categories.append('intermitentní aktivita')
    if any(word in typ_aktivity for word in ['generalized', 'generalizovaná']):
        categories.append('generalizovaná aktivita')
    if any(word in typ_aktivity for word in ['focal', 'fokální']):
        categories.append('fokální aktivita')
    if any(word in typ_aktivity for word in ['paroxysmální', 'paroxysmal']):
        categories.append('paroxysmální aktivita')
    if any(word in typ_aktivity for word in
           ['desynchronizace', 'desynchronization']):
        categories.append('desynchronizace')
    if any(word in typ_aktivity for word in ['komplex', 'complex']):
        categories.append('komplexní aktivita')
    if any(word in typ_aktivity for word in
           ['vysoká amplituda', 'high amplitude']):
        categories.append('vysoká amplituda')
    if any(word in typ_aktivity for word in
           ['nízká amplituda', 'low amplitude']):
        categories.append('nízká amplituda')
    if any(word in typ_aktivity for word in
           ['epileptiformní aktivita', 'epileptiform activity',
            'epileptický záchvat', 'epileptic seizure']):
        categories.append('epileptické aktivity')

    if not categories:
        categories.append('ostatní: ' + typ_aktivity)

    return ', '.join(categories)


def clean_pacientova_reakce(reakce):
    if pd.isna(reakce):
        return reakce
    reakce = reakce.lower().strip()

    if any(word in reakce for word in ['neuvozena']):
        return None

    categories = []

    if any(word in reakce for word in ['klidný', 'calm']):
        categories.append('klidný')
    if any(word in reakce for word in ['neklidný', 'restless']):
        categories.append('neklidný')
    if any(word in reakce for word in ['úzkost', 'anxiety']):
        categories.append('úzkost')
    if any(word in reakce for word in ['zmatený', 'confused']):
        categories.append('zmatený')
    if any(word in reakce for word in ['spavý', 'sleepy']):
        categories.append('spavý')
    if any(word in reakce for word in ['bdělý', 'awake']):
        categories.append('bdělý')
    if any(word in reakce for word in ['agresivní', 'aggressive']):
        categories.append('agresivní')
    if any(word in reakce for word in ['klonický', 'clonic']):
        categories.append('klonický')
    if any(word in reakce for word in ['tonický', 'tonic']):
        categories.append('tonický')
    if any(word in reakce for word in ['atypický', 'atypical']):
        categories.append('atypický')
    if any(word in reakce for word in ['normální', 'normal']):
        categories.append('normální')
    if any(word in reakce for word in ['apatie', 'apathy']):
        categories.append('apatie')
    if any(word in reakce for word in ['závratě', 'dizziness']):
        categories.append('závratě')
    if any(word in reakce for word in ['nevolnost', 'nausea']):
        categories.append('nevolnost')
    if any(word in reakce for word in ['hyperaktivní', 'hyperactive']):
        categories.append('hyperaktivní')
    if any(word in reakce for word in ['panika', 'panic']):
        categories.append('panika')
    if any(word in reakce for word in
           ['ztráta vědomí', 'loss of consciousness']):
        categories.append('ztráta vědomí')
    if any(word in reakce for word in ['podrážděný', 'irritable']):
        categories.append('podrážděný')

    if not categories:
        categories.append('ostatní: ' + reakce)

    return ', '.join(categories)


def clean_terapie_redukce(terapie):
    if pd.isna(terapie):
        return terapie
    terapie = terapie.lower().strip()

    categories = []

    if any(word in terapie for word in
           ['léky', 'antiepileptika', 'antiepileptický']):
        categories.append('léky')
    if any(word in terapie for word in ['antikonvulziva', 'antikonvulsiva']):
        categories.append('antikonvulziva')
    if any(word in terapie for word in ['chirurgie', 'operační', 'operace']):
        categories.append('chirurgie')
    if any(word in terapie for word in ['vns', 'vagus', 'nervová stimulace']):
        categories.append('vns')
    if any(word in terapie for word in ['ketogenní', 'dieta']):
        categories.append('ketogenní dieta')
    if any(word in terapie for word in ['dbs', 'hluboká stimulace mozku']):
        categories.append('dbs')
    if any(word in terapie for word in
           ['tms', 'transkraniální magnetická stimulace']):
        categories.append('tms')
    if any(word in terapie for word in
           ['psychoterapie', 'terapie', 'psycholog']):
        categories.append('psychoterapie')
    if any(word in terapie for word in
           ['cbt', 'kognitivně behaviorální terapie']):
        categories.append('cbt')
    if any(word in terapie for word in
           ['alternativní terapie', 'alternativní léčba']):
        categories.append('alternativní terapie')
    if any(word in terapie for word in ['biofeedback', 'biofeedback terapie']):
        categories.append('biofeedback')

    if not categories:
        categories.append('ostatní: ' + terapie)

    return ', '.join(categories)


# Process the presence of epileptic seizures
def detect_seizures(text):
    '''
    Analyzes the input text to determine if it indicates the presence or absence of seizures.

    1. Convert the input text to a string and lowercase it for case-insensitive comparison.
    2. Check if any seizure-indicating keywords or digits are present.
    3. If any of these keywords or digits are found, return True, indicating a seizure is detected.
    4. If absence-indicating keywords are found, return False, indicating no seizure is detected.
    5. If no keywords match, return the original processed text.
    '''

    text = str(text).lower()
    if any(keyword in text for keyword in
           ['masivní', 'záchvat', 'ano', 'přítomnost', 'přítomna',
            'přítomno', 'četné']) or any(
        char.isdigit() for char in text):
        return True
    if any(keyword in text for keyword in
           ['neuvozena', 'neuvedeno', 'ne', 'není']):
        return False
    return text
