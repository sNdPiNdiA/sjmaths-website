import os
import re
import json

BASE_DIR = r"ssc-cgl/general-awareness/geography"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'frs', 'fds', 'nri', 'pio', 'oci', 'caa', 'src', 'jvp', 'ist', 'gmt', 'utc', 'uv', 'co2', 'tisco', 'jnpt', 'nw', 'hp', 'up', 'jk', 'tn', 'ne', 'mp'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs', 'outside', 'between', 'or', 'life', 'major', 'era', 'sects', 'teachings', 'councils', 'findings', 'trade', 'sites', 'rig', 'later']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Enhanced, highly comprehensive mindmaps for all 5 CGL Geography folders
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. PHYSICAL GEOGRAPHY (Solar System, Earth Structure, Latitudes & Longitudes)
    if 'physical-geography-solar-system' in fl:
        return [
            {
                "label": "Solar System & Planetary Mechanics", "type": "branch", "date": "Cosmic Profile",
                "children": [
                    {
                        "label": "Inner Terrestrial Planets", "type": "sub", "date": "Inner Planets",
                        "children": [
                            {"label": "Sun: Hydrogen (71%) & Helium (26.5%); core temperature ~15 million K; energy via nuclear fusion (proton-proton chain)", "type": "leaf"},
                            {"label": "Mercury: Smallest, closest to Sun, no atmosphere, highest diurnal temperature range", "type": "leaf"},
                            {"label": "Venus: Earth's twin, hottest planet (due to 96% CO2 greenhouse effect), rotates clockwise (retrograde)", "type": "leaf"},
                            {"label": "Mars: Red planet (iron oxide), Olympus Mons (largest volcano in solar system), Phobos & Deimos moons", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Outer Jovian Planets", "type": "sub", "date": "Outer Gas Giants",
                        "children": [
                            {"label": "Jupiter: Largest planet, Great Red Spot, Ganymede moon (largest in solar system), Europa, Io, Callisto", "type": "leaf"},
                            {"label": "Saturn: Prominent rings, Titan moon (has dense atmosphere); Uranus: Tilted axis, methane atmosphere; Neptune: Coldest, Triton moon", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Earth & Moon Motions", "type": "sub", "date": "Earth/Moon Dynamics",
                        "children": [
                            {"label": "Rotation: 23.9 hours, causes day/night and Coriolis force; Revolution: 365.25 days, causes seasons and solstices/equinoxes", "type": "leaf"},
                            {"label": "Moon: Study called Selenology; light takes 1.3 seconds to reach Earth; tidal lock (only 59% visible from Earth)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Earth's Internal Structure & Rocks", "type": "branch", "date": "Lithosphere",
                "children": [
                    {
                        "label": "Concentric Layers", "type": "sub", "date": "Crust Mantle Core",
                        "children": [
                            {"label": "Crust (Sial): Silica & Aluminium; continental (granite, thicker) vs. oceanic (basalt, thinner); 1% of volume", "type": "leaf"},
                            {"label": "Mantle (Sima): Silica & Magnesium; upper mantle has Asthenosphere (magma source, plastic state); 84% volume", "type": "leaf"},
                            {"label": "Core (Nife): Nickel & Iron; outer core is liquid (creates magnetic field), inner core is solid; 15% volume", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Seismic Discontinuities", "type": "sub", "date": "Transition Zones",
                        "children": [
                            {"label": "Conrad (upper/lower crust), Mohorovicic (crust/mantle), Repetti (upper/lower mantle), Gutenberg (mantle/core), Lehmann (outer/inner core)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Rock Classifications", "type": "sub", "date": "Petrology",
                        "children": [
                            {"label": "Igneous: Formed from cooled magma; Granite (intrusive), Basalt (extrusive, forms black soil)", "type": "leaf"},
                            {"label": "Sedimentary: Stratified, contain fossils; Sandstone, Limestone, Shale, Coal", "type": "leaf"},
                            {"label": "Metamorphic: Marble (from Limestone), Quartzite (from Sandstone), Slate (from Shale), Gneiss (from Granite)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Latitudes, Longitudes & Time", "type": "branch", "date": "Grid System",
                "children": [
                    {
                        "label": "Latitudes (Parallels)", "type": "sub", "date": "Horizontal Lines",
                        "children": [
                            {"label": "Total 181 lines spaced at 111 km; Equator (0 deg), Tropics (23.5 deg N/S), Arctic/Antarctic (66.5 deg N/S)", "type": "leaf"},
                            {"label": "Horse Latitudes (30-35 deg N/S): Sub-tropical high pressure belts with calm winds and dry air", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Longitudes & Time Zones", "type": "sub", "date": "Vertical Meridians",
                        "children": [
                            {"label": "Total 360 meridians; 1 deg longitude = 4 minutes; Prime Meridian (0 deg) passes through Greenwich, London", "type": "leaf"},
                            {"label": "International Date Line (180 deg): Zig-zags to avoid land; crossing westwards adds a day, eastwards subtracts a day", "type": "leaf"},
                            {"label": "Indian Standard Time (IST): 82.5 deg E longitude, passes through Mirzapur (UP); 5.5 hours ahead of GMT (UTC+5:30)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Eclipses & Tides", "type": "sub", "date": "Astro-Phenomena",
                        "children": [
                            {"label": "Solar Eclipse: Moon between Sun & Earth (New Moon); Lunar Eclipse: Earth between Sun & Moon (Full Moon)", "type": "leaf"},
                            {"label": "Spring Tides: Sun, Moon, Earth in straight line (Syzygy, highest tides); Neap Tides: Right angle alignment (lowest tides)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. CLIMATOLOGY & OCEANOGRAPHY (Wind Systems, Currents, Rainfall)
    elif 'climatology-oceanography' in fl:
        return [
            {
                "label": "Atmosphere & Weather Parameters", "type": "branch", "date": "Climatology",
                "children": [
                    {
                        "label": "Atmospheric Layers", "type": "sub", "date": "Structure",
                        "children": [
                            {"label": "Troposphere: Densest, weather phenomena, temperature drops with height (6.5C/km normal lapse rate)", "type": "leaf"},
                            {"label": "Stratosphere: Ozone layer (absorbs UV); free of clouds, ideal for flying jet aircraft", "type": "leaf"},
                            {"label": "Mesosphere: Coldest layer (-100C), meteors burn up; Ionosphere: Reflects radio waves, Auroras occur here", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Pressure Belts & Coriolis", "type": "sub", "date": "Forces",
                        "children": [
                            {"label": "Belts: Equatorial Low (Doldrums, 0-5 deg N/S), Sub-tropical Highs (30-35 deg), Sub-polar Lows (60-65 deg), Polar Highs", "type": "leaf"},
                            {"label": "Coriolis Force: Ferrel's Law; winds deflect to right in Northern hemisphere, left in Southern hemisphere", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Humidity & Clouds", "type": "sub", "date": "Humidity",
                        "children": [
                            {"label": "Relative Humidity measured by Hygrometer; absolute humidity is actual water vapor mass per unit volume", "type": "leaf"},
                            {"label": "Clouds: Cirrus (high, ice crystals), Cumulus (cotton-like, fair weather), Stratus (low, layered), Nimbus (dark, rain)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Wind Systems & Cyclones", "type": "branch", "date": "Atmospheric Circulation",
                "children": [
                    {
                        "label": "Planetary Winds", "type": "sub", "date": "Global Winds",
                        "children": [
                            {"label": "Trade Winds: Blow from Sub-tropical Highs to Equatorial Low; Westerlies: Blow to Sub-polar Lows (Roaring Forties, Furious Fifties)", "type": "leaf"},
                            {"label": "Polar Easterlies: Dry and extremely cold winds blowing from Polar Highs", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Local Winds", "type": "sub", "date": "Hot & Cold",
                        "children": [
                            {"label": "Hot: Loo (North India plains), Fohn (Alps), Chinook (Rockies, snow eater), Harmattan (West Africa, doctor wind)", "type": "leaf"},
                            {"label": "Cold: Mistral (France), Bora (Adriatic Sea), Pampero (Argentina), Blizzard (Canada/Siberia)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Cyclones & Anticyclones", "type": "sub", "date": "Storm Systems",
                        "children": [
                            {"label": "Cyclones: Low-pressure center; winds rotate counter-clockwise in North, clockwise in South", "type": "leaf"},
                            {"label": "Local names: Hurricanes (Atlantic), Typhoons (China Sea), Willy-Willies (Australia), Cyclones (Indian Ocean)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Oceanography & Currents", "type": "branch", "date": "Oceanography",
                "children": [
                    {
                        "label": "Relief & Salinity", "type": "sub", "date": "Ocean Relief",
                        "children": [
                            {"label": "Relief: Continental Shelf -> Slope -> Rise -> Abyssal Plain -> Trenches (Mariana Challenger Deep is deepest)", "type": "leaf"},
                            {"label": "Salinity: Average 35 ppt; highest in Lake Van (Turkey, 330 ppt), Dead Sea (238 ppt), Great Salt Lake (USA)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Ocean Currents", "type": "sub", "date": "Warm & Cold",
                        "children": [
                            {"label": "Atlantic: Warm Gulf Stream, North Atlantic Drift; Cold Labrador current, Canary, Benguela", "type": "leaf"},
                            {"label": "Pacific: Warm Kuroshio (Black Stream); Cold Oyashio (Kuril), Peru (Humboldt) current, California", "type": "leaf"},
                            {"label": "Indian: Warm Agulhas, Mozambique; Cold West Australian current", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Trenches & Ridges", "type": "sub", "date": "Underwater Relief",
                        "children": [
                            {"label": "Mariana Trench (Pacific, 11022m), Puerto Rico Trench (Atlantic), Sunda/Java Trench (Indian Ocean)", "type": "leaf"},
                            {"label": "Mid-Atlantic Ridge: S-shaped submarine mountain range extending along the Atlantic Ocean floor", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. WORLD GEOGRAPHY (Continents, Deserts, Straits, Canals, Rivers)
    elif 'world-geography-continents' in fl:
        return [
            {
                "label": "Continents, Peaks & Grasslands", "type": "branch", "date": "World Relief",
                "children": [
                    {
                        "label": "Continental Profiles", "type": "sub", "date": "Continents",
                        "children": [
                            {"label": "Asia: Largest, highest point Mt Everest (8848m), lowest point Dead Sea (-430m); Africa: Second largest, crossed by Equator, Cancer, and Capricorn", "type": "leaf"},
                            {"label": "North America: Denali peak; South America: Andes range (longest), Aconcagua peak; Europe: Volga longest river, no deserts", "type": "leaf"},
                            {"label": "Australia: Smallest, flat relief, Great Dividing Range; Antarctica: Coldest, highest average elevation", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "World Grasslands", "type": "sub", "date": "Grasslands",
                        "children": [
                            {"label": "Temperate: Prairies (North America), Pampas (Argentina), Steppes (Eurasia), Downs (Australia), Velds (South Africa)", "type": "leaf"},
                            {"label": "Tropical: Savannahs (Africa), Llanos (Venezuela), Campos (Brazil)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Straits, Canals & Deserts", "type": "branch", "date": "World Channels",
                "children": [
                    {
                        "label": "Straits & Canals", "type": "sub", "date": "Chokepoints",
                        "children": [
                            {"label": "Strait of Malacca (Andaman/South China Sea); Gibraltar (Mediterranean/Atlantic); Bab-el-Mandeb (Red Sea/Gulf of Aden)", "type": "leaf"},
                            {"label": "Suez Canal (1869): Connects Mediterranean & Red Sea; Panama Canal (1914): Connects Atlantic & Pacific Oceans", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Deserts", "type": "sub", "date": "Arid Zones",
                        "children": [
                            {"label": "Hot: Sahara (largest hot), Thar (most populous), Atacama (driest, Chile), Kalahari (Botswana, Bushmen)", "type": "leaf"},
                            {"label": "Cold: Gobi (Mongolia/China), Patagonia (Argentina), Great Basin (USA), Antarctic & Arctic (largest overall)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "World Rivers & Lakes", "type": "branch", "date": "Hydrology",
                "children": [
                    {
                        "label": "River Systems & Lakes", "type": "sub", "date": "Waterbodies",
                        "children": [
                            {"label": "Rivers: Nile (longest, Victoria origin), Amazon (largest by volume), Mississippi-Missouri (bird's foot delta), Yangtze (longest in Asia)", "type": "leaf"},
                            {"label": "Lakes: Caspian Sea (largest lake), Lake Superior (largest freshwater), Baikal (deepest, Siberia), Titicaca (highest navigable)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Cities on Rivers", "type": "sub", "date": "Urban Rivers",
                        "children": [
                            {"label": "London (Thames), Paris (Seine), New York (Hudson), Rome (Tiber), Cairo (Nile), Baghdad (Tigris), Vienna/Budapest (Danube)", "type": "leaf"},
                            {"label": "Victoria Falls (Zambezi river, Africa); Angel Falls (Venezuela, highest waterfall in the world)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. INDIAN GEOGRAPHY (Rivers, Climate, Soils, Forests, Mountains)
    elif 'indian-geography-rivers' in fl:
        return [
            {
                "label": "Mountains & Mountain Passes", "type": "branch", "date": "Indian Relief",
                "children": [
                    {
                        "label": "Himalayas & North Peaks", "type": "sub", "date": "North Mountains",
                        "children": [
                            {"label": "Himadri (Great, 6000m): Mt Everest, Kanchenjunga (highest in undisputed India); Himachal (Lesser), Shiwaliks (Outer)", "type": "leaf"},
                            {"label": "Karakoram: Godwin Austen (K2, 8611m, highest peak in India/PoK); Siachen Glacier is located here", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Peninsular Ranges & Peaks", "type": "sub", "date": "South Mountains",
                        "children": [
                            {"label": "Western Ghats (Sahyadri): Continuous; highest peak Anamudi (2695m, Kerala); meet Eastern Ghats at Nilgiris (Doddabetta)", "type": "leaf"},
                            {"label": "Aravallis: Oldest fold mountains, highest Guru Shikhar (1722m); Satpuras: Block mountains, highest Dhupgarh (1350m)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Important Mountain Passes", "type": "sub", "date": "Passes",
                        "children": [
                            {"label": "Northern: Zoji La (J&K), Shipki La (HP, Sutlej enters India here), Bara-lacha La (HP), Nathu La & Jelep La (Sikkim)", "type": "leaf"},
                            {"label": "Peninsular: Thalghat (Mumbai-Nashik), Bhorghat (Mumbai-Pune), Palghat (Coimbatore-Palakkad in Nilgiris)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Indian River Systems", "type": "branch", "date": "Indian Rivers",
                "children": [
                    {
                        "label": "Himalayan Rivers", "type": "sub", "date": "North Rivers",
                        "children": [
                            {"label": "Ganga: Originates as Bhagirathi at Gangotri, joins Alaknanda at Devprayag; tributaries Yamuna, Son, Gandak, Kosi (Sorrow of Bihar)", "type": "leaf"},
                            {"label": "Indus: Mansarovar origin; tributaries Jhelum, Chenab (largest), Ravi, Beas, Sutlej; Brahmaputra: Tsangpo in Tibet, enters at Namcha Barwa, forms Majuli island", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Peninsular Rivers", "type": "sub", "date": "South Rivers",
                        "children": [
                            {"label": "East Flowing: Godavari (Dakshin Ganga, longest peninsular), Krishna, Kaveri (perennial flow due to double monsoon), Mahanadi", "type": "leaf"},
                            {"label": "West Flowing: Narmada (rift valley flow between Vindhyas/Satpuras), Tapi (rift valley), Sabarmati, Mahi (crosses Tropic of Cancer twice)", "type": "leaf"}
                        ]
                    },
                    {
                        "River Projects & Waterfalls": "sub", "date": "River Engineering",
                        "children": [
                            {"label": "Projects: Bhakra Nangal (Sutlej), Tehri (Bhagirathi, highest dam), Hirakud (Mahanadi, longest dam), Nagarjuna Sagar (Krishna)", "type": "leaf"},
                            {"label": "Waterfalls: Jog/Gersoppa Falls (Sharavati, Karnataka), Kunchikal Falls (Varahi, Karnataka, highest tiered waterfall)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Soils, Forests & Monsoons", "type": "branch", "date": "Soils & Weather",
                "children": [
                    {
                        "label": "Soils of India (ICAR)", "type": "sub", "date": "Soils",
                        "children": [
                            {"label": "Alluvial (43%): Richest, Northern plains; Khadar (new, fertile) vs. Bhangar (old, clayey, kankar)", "type": "leaf"},
                            {"label": "Black (Regur, 15%): Basaltic Deccan trap, high moisture retention, self-ploughing, ideal for Cotton", "type": "leaf"},
                            {"label": "Red Soil: High iron content (hydrated yellow); Laterite: High leaching, acidic, ideal for Cashew, Tea, Coffee", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Monsoons & Natural Vegetation", "type": "sub", "date": "Climate",
                        "children": [
                            {"label": "Tropical Deciduous Forests: Most widespread in India; Teak, Sal, Bamboo, Sandalwood (Monsoon Forests)", "type": "leaf"},
                            {"label": "Tropical Evergreen: Western Ghats, NE India (Ebony, Mahogany, Rosewood); Mangroves: Sundarbans (pneumatophores)", "type": "leaf"},
                            {"label": "Monsoons: Southwest monsoon (June-Sept) advances in Arabian Sea/Bay of Bengal branches; Northeast (Oct-Dec) brings rain to Coromandel (TN)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. INDIAN RESOURCES (Agriculture, Minerals, Energy, Industries, Ports)
    elif 'indian-resources-agriculture' in fl:
        return [
            {
                "label": "Agriculture & State Rankings", "type": "branch", "date": "Agronomy",
                "children": [
                    {
                        "label": "Cropping Seasons", "type": "sub", "date": "Seasons",
                        "children": [
                            {"label": "Kharif: Sown June/July, harvested Oct/Nov; Rice, Maize, Cotton, Jute, Groundnut; needs high temp/rain", "type": "leaf"},
                            {"label": "Rabi: Sown Oct/Nov, harvested March/April; Wheat, Barley, Mustard, Gram, Peas; needs cool climate", "type": "leaf"},
                            {"label": "Zaid: Sown March to June (summer crops); Watermelon, Cucumber, Fodder crops", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Revolutions", "type": "sub", "date": "Agricultural Tech",
                        "children": [
                            {"label": "Green Revolution (1966-67): M.S. Swaminathan (India); HYV seeds, chemical fertilizers, irrigation; focus on Wheat & Rice", "type": "leaf"},
                            {"label": "White Revolution (Verghese Kurien, Operation Flood, Milk); Yellow (Oilseeds); Blue (Fish); Golden (Horticulture)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Crop Production State Rankings", "type": "sub", "date": "Rankings",
                        "children": [
                            {"label": "Leading States: Rice (West Bengal), Wheat & Sugarcane (UP), Cotton (Gujarat), Jute (West Bengal), Coffee (Karnataka), Rubber (Kerala)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Minerals & Energy Resources", "type": "branch", "date": "Energy",
                "children": [
                    {
                        "label": "Metallic & Non-Metallic Minerals", "type": "sub", "date": "Mining Areas",
                        "children": [
                            {"label": "Iron Ore: Odisha (largest producer), Jharkhand (Noamundi), Chhattisgarh (Bailadila hematite), Karnataka (Kudremukh)", "type": "leaf"},
                            {"label": "Bauxite: Odisha (Panchpatmali) leading; Copper: Khetri (Rajasthan) famous mines; Manganese: MP leading", "type": "leaf"},
                            {"label": "Mica: Andhra Pradesh (Nellore district is leading producer); Gold: Kolar Gold Fields (KGF, Karnataka)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Coal, Petroleum & Nuclear", "type": "sub", "date": "Fossil Fuels",
                        "children": [
                            {"label": "Coal: Gondwana coal (98% reserves, bituminous); Jharia (Jharkhand) largest field; Raniganj (WB) oldest field", "type": "leaf"},
                            {"label": "Petroleum: Digboi (Assam, oldest well 1889); Mumbai High (largest producer); KG Basin (gas reserves)", "type": "leaf"},
                            {"label": "Nuclear: Uranium in Jaduguda (Jharkhand); Thorium in Monazite sands of Kerala coast", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Industries, Ports & Waterways", "type": "branch", "date": "Infrastructure",
                "children": [
                    {
                        "label": "Industrial Centers", "type": "sub", "date": "Clusters",
                        "children": [
                            {"label": "Iron & Steel: TISCO (Jamshedpur, 1907); Bhilai (USSR aid), Rourkela (Germany aid), Durgapur (UK aid), Bokaro (USSR)", "type": "leaf"},
                            {"label": "Cotton: Mumbai (Cottonpolis of India), Ahmedabad (Manchester of India), Coimbatore (Manchester of South)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Major Seaports", "type": "sub", "date": "13 Major Ports",
                        "children": [
                            {"label": "Kandla (Deendayal, Gujarat): Tidal port, tax-free zone; Mumbai: Largest and busiest natural port", "type": "leaf"},
                            {"label": "JNPT (Nhava Sheva): Largest container port, fully automated; Visakhapatnam: Deepest landlocked protected port", "type": "leaf"},
                            {"label": "Chennai: Oldest artificial port; Kolkata (Syama Prasad): Riverine port; Marmagao (Goa): Iron exports", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "National Waterways", "type": "sub", "date": "Waterways",
                        "children": [
                            {"label": "NW-1: Prayagraj to Haldia (Ganga-Bhagirathi-Hooghly, longest NW in India); NW-2: Sadiya to Dhubri (Brahmaputra)", "type": "leaf"},
                            {"label": "NW-3: Kottapuram to Kollam (West Coast Canal, Kerala)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    raise Exception(f"Folder '{folder_name}' has no custom mindmap branch mapped!")

# Patching Logic
def patch_html(filepath, tree_data, title_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Clean previous mindmap tags to prevent duplicates (using ?v=3 to force cache bypass)
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    mindmap_div_pattern = r'            <!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '<!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    script_pattern = r'    <!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    # Re-inject CSS
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    # Re-inject Mindmap Div
    instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand — opening one automatically closes its siblings.'
    mindmap_card = f'''            <!-- Interactive Mindmap -->
            <div class="card-premium" id="mindmap-card">
                <h2 class="card-title"><i class="fas fa-diagram-project"></i> {title_text}</h2>
                <p style="color:var(--text-light);font-size:.87rem;margin-bottom:1.25rem;">
                    <i class="fas fa-circle-info" style="color:#8b5cf6;margin-right:5px;"></i>
                    {instr}
                </p>
                <div id="prehistory-mindmap-container"></div>
            </div>
            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->
'''
    # We find "<!-- Prep Tracker -->" or fallback
    prep_tracker = "        <!-- Prep Tracker -->"
    if prep_tracker in html:
        html = html.replace(prep_tracker, mindmap_card + "\n" + prep_tracker, 1)
    else:
        # Fallback to checklist
        checklist_marker = '<div class="card-premium">'
        # Let's replace the first one that comes after Key Concepts
        pos = html.find('Self-Evaluation Checklist')
        if pos != -1:
            # find the card-premium preceding it
            card_pos = html.rfind('<div class="card-premium">', 0, pos)
            if card_pos != -1:
                html = html[:card_pos] + mindmap_card + "\n" + html[card_pos:]

    # Re-inject script with ?v=3 to force reload of wrapping logic
    tree_json = json.dumps(tree_data)
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=3"></script>
    <script>
    renderMindmap({tree_json}, undefined, 'en');
    </script>
'''
    html = html.replace('</body>', inline_script + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  Successfully patched: {filepath}")
    return True

# Main execution
def main():
    folders = sorted([f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f))])
    print(f"Found {len(folders)} topics to process.")
    
    for idx, folder in enumerate(folders):
        folder_path = os.path.join(BASE_DIR, folder)
        html_path = os.path.join(folder_path, 'index.html')
        content_path = os.path.join(folder_path, 'content.json')
        
        if not os.path.exists(html_path):
            print(f"[{idx+1}/{len(folders)}] Skipping {folder} (index.html not found)")
            continue
            
        topic_name = get_clean_title(folder)
        if os.path.exists(content_path):
            try:
                with open(content_path, 'r', encoding='utf-8') as f:
                    content_data = json.load(f)
                    topic_name = content_data.get('hero', {}).get('title', topic_name)
            except Exception:
                pass
        
        # Build custom, 3-tier deep-dive topic-specific mindmap data
        branches = get_custom_branches(folder)
        mindmap_data = {
            "label": get_clean_title(folder),
            "type": "root",
            "children": branches
        }
        
        title_text = f"{topic_name} &mdash; Interactive Mindmap"
        success = patch_html(html_path, mindmap_data, title_text)
        if success:
            print(f"[{idx+1}/{len(folders)}] Processed {folder}")
        else:
            print(f"[{idx+1}/{len(folders)}] Failed to patch {folder}")

if __name__ == '__main__':
    main()
