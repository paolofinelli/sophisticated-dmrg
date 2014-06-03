#!/usr/bin/env python

from sophisticated_dmrg import HeisenbergXXZChain, finite_system_algorithm, open_bc, periodic_bc

# expected results are taken from exact diagonalization

expected_energy = {
    open_bc: -5.63552961749324,
    periodic_bc: -5.75814398110789,
}
expected_Sz = {
    open_bc: {
        0: 0.380927022651224,
        1: -0.136056762511492,
        2: 0.118088125191709,
        3: -0.324427554030101,
        4: -0.0293082646011701,
        5: 0.080280872605819,
        6: 0.107382672186401,
        7: -0.196379958994102,
        8: 0.189553312888283,
        9: -0.203159954875788,
        10: -0.190071091118365,
        11: 0.203171580607582,
    },
    periodic_bc: {
        0: 0.251970534661742,
        1: -0.014905816107976,
        2: 0.0138790327761257,
        3: -0.274704496076216,
        4: 0.016042987433838,
        5: 0.067019907241627,
        6: 0.107468173924465,
        7: -0.231028029504729,
        8: 0.25946797753064,
        9: -0.236502949591289,
        10: 0.0575550494278513,
        11: -0.0162623717160799,
    },
}
expected_Sz_Sz = {
    open_bc: {
        (0, 0): 0.250000000000003,
        (0, 1): -0.126221187261807,
        (0, 2): 0.0443942828827648,
        (0, 3): -0.144885160715301,
        (0, 4): -0.00277611796409998,
        (0, 5): 0.019921122619248,
        (0, 6): 0.0444460389387958,
        (0, 7): -0.0816634579877597,
        (0, 8): 0.0754800493441368,
        (0, 9): -0.0823284490754211,
        (0, 10): -0.0713711415016831,
        (0, 11): 0.0750040207211232,
        (1, 0): -0.126221187261807,
        (1, 1): 0.250000000000003,
        (1, 2): -0.166135440836618,
        (1, 3): 0.0493678830282252,
        (1, 4): 0.00481254874416006,
        (1, 5): -0.0149862613351064,
        (1, 6): -0.0168749629002306,
        (1, 7): 0.0220704553195463,
        (1, 8): -0.0238677691507445,
        (1, 9): 0.0243437577921975,
        (1, 10): 0.0267673847910734,
        (1, 11): -0.0292764081906997,
        (2, 0): 0.0443942828827648,
        (2, 1): -0.166135440836618,
        (2, 2): 0.250000000000003,
        (2, 3): -0.123696769975193,
        (2, 4): 0.00947211939657975,
        (2, 5): -0.004387975617772,
        (2, 6): 0.0200553848794982,
        (2, 7): -0.0279319539144804,
        (2, 8): 0.02467555794653,
        (2, 9): -0.0270251675190035,
        (2, 10): -0.0220609403011598,
        (2, 11): 0.0226409030588511,
        (3, 0): -0.144885160715301,
        (3, 1): 0.0493678830282252,
        (3, 2): -0.123696769975193,
        (3, 3): 0.250000000000003,
        (3, 4): -0.0436421178972396,
        (3, 5): -0.00857574259218155,
        (3, 6): -0.0483305916506317,
        (3, 7): 0.0685888352235739,
        (3, 8): -0.0644175946079963,
        (3, 9): 0.0689344500167698,
        (3, 10): 0.061239715263393,
        (3, 11): -0.0645829060934216,
        (4, 0): -0.00277611796409998,
        (4, 1): 0.00481254874416006,
        (4, 2): 0.00947211939657975,
        (4, 3): -0.0436421178972396,
        (4, 4): 0.250000000000003,
        (4, 5): -0.184816900536818,
        (4, 6): 0.0320794358485881,
        (4, 7): -0.0487543774015821,
        (4, 8): 0.016760800001719,
        (4, 9): -0.0254251381307306,
        (4, 10): 0.0123521524453922,
        (4, 11): -0.0200624045059725,
        (5, 0): 0.019921122619248,
        (5, 1): -0.0149862613351064,
        (5, 2): -0.004387975617772,
        (5, 3): -0.00857574259218155,
        (5, 4): -0.184816900536818,
        (5, 5): 0.250000000000003,
        (5, 6): -0.0886642798874285,
        (5, 7): 0.0253300389687851,
        (5, 8): -0.00412142272581209,
        (5, 9): 0.00476055009358912,
        (5, 10): -0.0198849302737381,
        (5, 11): 0.025425801287231,
        (6, 0): 0.0444460389387958,
        (6, 1): -0.0168749629002306,
        (6, 2): 0.0200553848794982,
        (6, 3): -0.0483305916506317,
        (6, 4): 0.0320794358485881,
        (6, 5): -0.0886642798874285,
        (6, 6): 0.250000000000003,
        (6, 7): -0.173029161705678,
        (6, 8): 0.0609907922578787,
        (6, 9): -0.0714135684482618,
        (6, 10): -0.011775625817614,
        (6, 11): 0.00251653848508151,
        (7, 0): -0.0816634579877597,
        (7, 1): 0.0220704553195463,
        (7, 2): -0.0279319539144804,
        (7, 3): 0.0685888352235739,
        (7, 4): -0.0487543774015821,
        (7, 5): 0.0253300389687851,
        (7, 6): -0.173029161705678,
        (7, 7): 0.250000000000003,
        (7, 8): -0.120369637723445,
        (7, 9): 0.0839802323956296,
        (7, 10): 0.0257895063248239,
        (7, 11): -0.0240104794994157,
        (8, 0): 0.0754800493441368,
        (8, 1): -0.0238677691507445,
        (8, 2): 0.02467555794653,
        (8, 3): -0.0644175946079963,
        (8, 4): 0.016760800001719,
        (8, 5): -0.00412142272581209,
        (8, 6): 0.0609907922578787,
        (8, 7): -0.120369637723445,
        (8, 8): 0.250000000000003,
        (8, 9): -0.20447566943872,
        (8, 10): -0.0103066955844427,
        (8, 11): -0.000348410319107052,
        (9, 0): -0.0823284490754211,
        (9, 1): 0.0243437577921975,
        (9, 2): -0.0270251675190035,
        (9, 3): 0.0689344500167698,
        (9, 4): -0.0254251381307306,
        (9, 5): 0.00476055009358912,
        (9, 6): -0.0714135684482618,
        (9, 7): 0.0839802323956296,
        (9, 8): -0.20447566943872,
        (9, 9): 0.250000000000003,
        (9, 10): -0.0123968840442135,
        (9, 11): -0.00895411364183893,
        (10, 0): -0.0713711415016831,
        (10, 1): 0.0267673847910734,
        (10, 2): -0.0220609403011598,
        (10, 3): 0.061239715263393,
        (10, 4): 0.0123521524453922,
        (10, 5): -0.0198849302737381,
        (10, 6): -0.011775625817614,
        (10, 7): 0.0257895063248239,
        (10, 8): -0.0103066955844427,
        (10, 9): -0.0123968840442135,
        (10, 10): 0.250000000000003,
        (10, 11): -0.228352541301834,
        (11, 0): 0.0750040207211232,
        (11, 1): -0.0292764081906997,
        (11, 2): 0.0226409030588511,
        (11, 3): -0.0645829060934216,
        (11, 4): -0.0200624045059725,
        (11, 5): 0.025425801287231,
        (11, 6): 0.00251653848508151,
        (11, 7): -0.0240104794994157,
        (11, 8): -0.000348410319107052,
        (11, 9): -0.00895411364183893,
        (11, 10): -0.228352541301834,
        (11, 11): 0.250000000000003,
    },
    periodic_bc: {
        (0, 0): 0.250000000000002,
        (0, 1): -0.0948097047285464,
        (0, 2): 0.0317505952964268,
        (0, 3): -0.0967567018203554,
        (0, 4): 0.0162116835649695,
        (0, 5): 0.00149409649794003,
        (0, 6): 0.0423706517828481,
        (0, 7): -0.0733589121869654,
        (0, 8): 0.0788434878374333,
        (0, 9): -0.0883253601880022,
        (0, 10): 0.0340647567836856,
        (0, 11): -0.101484592839436,
        (1, 0): -0.0948097047285464,
        (1, 1): 0.250000000000002,
        (1, 2): -0.175111575226115,
        (1, 3): 0.0282776445697974,
        (1, 4): -0.0111241876313048,
        (1, 5): 0.00459950022381238,
        (1, 6): -0.0214893056584108,
        (1, 7): 0.00691565687996494,
        (1, 8): -0.0124786001392513,
        (1, 9): 0.0148990682539378,
        (1, 10): -0.00960632965949583,
        (1, 11): 0.0199278331156101,
        (2, 0): 0.0317505952964268,
        (2, 1): -0.175111575226115,
        (2, 2): 0.250000000000002,
        (2, 3): -0.089452159749666,
        (2, 4): 0.0131785070943147,
        (2, 5): -0.013878194993777,
        (2, 6): 0.0185159986221862,
        (2, 7): -0.0102806765400002,
        (2, 8): 0.00959678515398784,
        (2, 9): -0.0164749639135959,
        (2, 10): -0.00100303270555681,
        (2, 11): -0.0168412830382062,
        (3, 0): -0.0967567018203554,
        (3, 1): 0.0282776445697974,
        (3, 2): -0.089452159749666,
        (3, 3): 0.250000000000002,
        (3, 4): -0.0930788242020511,
        (3, 5): 0.00971420235789359,
        (3, 6): -0.0646050129713476,
        (3, 7): 0.0757397481064414,
        (3, 8): -0.0865628793117161,
        (3, 9): 0.0779696730009117,
        (3, 10): -0.0301730264110209,
        (3, 11): 0.0189273364311113,
        (4, 0): 0.0162116835649695,
        (4, 1): -0.0111241876313048,
        (4, 2): 0.0131785070943147,
        (4, 3): -0.0930788242020511,
        (4, 4): 0.250000000000002,
        (4, 5): -0.155883028146471,
        (4, 6): 0.0289733038239265,
        (4, 7): -0.0432154413327269,
        (4, 8): 0.0205541574692712,
        (4, 9): -0.0235689305646957,
        (4, 10): 0.016885870822518,
        (4, 11): -0.0189331108977525,
        (5, 0): 0.00149409649794003,
        (5, 1): 0.00459950022381238,
        (5, 2): -0.013878194993777,
        (5, 3): 0.00971420235789359,
        (5, 4): -0.155883028146471,
        (5, 5): 0.250000000000002,
        (5, 6): -0.112633836795471,
        (5, 7): 0.021181867142089,
        (5, 8): -0.00709414272531618,
        (5, 9): 0.00195153075048392,
        (5, 10): -0.0132474736007826,
        (5, 11): 0.0137954792895957,
        (6, 0): 0.0423706517828481,
        (6, 1): -0.0214893056584108,
        (6, 2): 0.0185159986221862,
        (6, 3): -0.0646050129713476,
        (6, 4): 0.0289733038239265,
        (6, 5): -0.112633836795471,
        (6, 6): 0.250000000000002,
        (6, 7): -0.144604381285307,
        (6, 8): 0.0628195068612626,
        (6, 9): -0.0592733890613476,
        (6, 10): 0.021527878295374,
        (6, 11): -0.0216014136137154,
        (7, 0): -0.0733589121869654,
        (7, 1): 0.00691565687996494,
        (7, 2): -0.0102806765400002,
        (7, 3): 0.0757397481064414,
        (7, 4): -0.0432154413327269,
        (7, 5): 0.021181867142089,
        (7, 6): -0.144604381285307,
        (7, 7): 0.250000000000002,
        (7, 8): -0.154323757349207,
        (7, 9): 0.0890830352801109,
        (7, 10): -0.0398906861503054,
        (7, 11): 0.0227535474359047,
        (8, 0): 0.0788434878374333,
        (8, 1): -0.0124786001392513,
        (8, 2): 0.00959678515398784,
        (8, 3): -0.0865628793117161,
        (8, 4): 0.0205541574692712,
        (8, 5): -0.00709414272531618,
        (8, 6): 0.0628195068612626,
        (8, 7): -0.154323757349207,
        (8, 8): 0.250000000000002,
        (8, 9): -0.173880927079871,
        (8, 10): 0.0499271888282659,
        (8, 11): -0.0374008195448612,
        (9, 0): -0.0883253601880022,
        (9, 1): 0.0148990682539378,
        (9, 2): -0.0164749639135959,
        (9, 3): 0.0779696730009117,
        (9, 4): -0.0235689305646957,
        (9, 5): 0.00195153075048392,
        (9, 6): -0.0592733890613476,
        (9, 7): 0.0890830352801109,
        (9, 8): -0.173880927079871,
        (9, 9): 0.250000000000002,
        (9, 10): -0.110860953171183,
        (9, 11): 0.0384812166932486,
        (10, 0): 0.0340647567836856,
        (10, 1): -0.00960632965949583,
        (10, 2): -0.00100303270555681,
        (10, 3): -0.0301730264110209,
        (10, 4): 0.016885870822518,
        (10, 5): -0.0132474736007826,
        (10, 6): 0.021527878295374,
        (10, 7): -0.0398906861503054,
        (10, 8): 0.0499271888282659,
        (10, 9): -0.110860953171183,
        (10, 10): 0.250000000000002,
        (10, 11): -0.167624193031501,
        (11, 0): -0.101484592839436,
        (11, 1): 0.0199278331156101,
        (11, 2): -0.0168412830382062,
        (11, 3): 0.0189273364311113,
        (11, 4): -0.0189331108977525,
        (11, 5): 0.0137954792895957,
        (11, 6): -0.0216014136137154,
        (11, 7): 0.0227535474359047,
        (11, 8): -0.0374008195448612,
        (11, 9): 0.0384812166932486,
        (11, 10): -0.167624193031501,
        (11, 11): 0.250000000000002,
    },
}
expected_Sp_Sm = {
    open_bc: {
        (0, 0): 0.88092702265123,
        (0, 1): -0.262661506108124,
        (0, 2): 0.14116753056054,
        (0, 3): -0.106499804009335,
        (0, 4): 0.0534885199582284,
        (0, 5): -0.0547254730183054,
        (0, 6): 0.0389136440318317,
        (0, 7): -0.0378000406208441,
        (0, 8): 0.0203259967167556,
        (0, 9): -0.0275377468671827,
        (0, 10): 0.0154459653416028,
        (0, 11): -0.0157191000551504,
        (1, 0): -0.262661506108124,
        (1, 1): 0.363943237488514,
        (1, 2): -0.366347661131153,
        (1, 3): 0.141599656140122,
        (1, 4): -0.0721219511685196,
        (1, 5): 0.0685010854327646,
        (1, 6): -0.0544684997020737,
        (1, 7): 0.0486077728360587,
        (1, 8): -0.0256826119248349,
        (1, 9): 0.0333219425519274,
        (1, 10): -0.0178401278243851,
        (1, 11): 0.0186595479705245,
        (2, 0): 0.14116753056054,
        (2, 1): -0.366347661131153,
        (2, 2): 0.618088125191715,
        (2, 3): -0.259969594962114,
        (2, 4): 0.0937046061087862,
        (2, 5): -0.0860700033246551,
        (2, 6): 0.0555686574971302,
        (2, 7): -0.0525756084128191,
        (2, 8): 0.0277749850981131,
        (2, 9): -0.0371363305270252,
        (2, 10): 0.0207197497937901,
        (2, 11): -0.0209779658795406,
        (3, 0): -0.106499804009335,
        (3, 1): 0.141599656140122,
        (3, 2): -0.259969594962114,
        (3, 3): 0.175572445969905,
        (3, 4): -0.169464482183663,
        (3, 5): 0.111097295542631,
        (3, 6): -0.0849996732052932,
        (3, 7): 0.068779985708525,
        (3, 8): -0.0351402135149769,
        (3, 9): 0.0435247904047193,
        (3, 10): -0.0224463805679564,
        (3, 11): 0.0237387702508952,
        (4, 0): 0.0534885199582284,
        (4, 1): -0.0721219511685196,
        (4, 2): 0.0937046061087862,
        (4, 3): -0.169464482183663,
        (4, 4): 0.470691735398836,
        (4, 5): -0.392796787620917,
        (4, 6): 0.162724720948378,
        (4, 7): -0.146937171125042,
        (4, 8): 0.0685925655317263,
        (4, 9): -0.0890076598318992,
        (4, 10): 0.0461514107515209,
        (4, 11): -0.0477428675615197,
        (5, 0): -0.0547254730183054,
        (5, 1): 0.0685010854327646,
        (5, 2): -0.0860700033246551,
        (5, 3): 0.111097295542631,
        (5, 4): -0.392796787620917,
        (5, 5): 0.580280872605825,
        (5, 6): -0.23038885285509,
        (5, 7): 0.113635799710859,
        (5, 8): -0.0572352443782531,
        (5, 9): 0.0632405366018826,
        (5, 10): -0.0330514824586447,
        (5, 11): 0.0334449788720193,
        (6, 0): 0.0389136440318317,
        (6, 1): -0.0544684997020737,
        (6, 2): 0.0555686574971302,
        (6, 3): -0.0849996732052932,
        (6, 4): 0.162724720948378,
        (6, 5): -0.23038885285509,
        (6, 6): 0.607382672186407,
        (6, 7): -0.346290824830012,
        (6, 8): 0.108283552025865,
        (6, 9): -0.13356906288566,
        (6, 10): 0.0665814977597425,
        (6, 11): -0.066080213271577,
        (7, 0): -0.0378000406208441,
        (7, 1): 0.0486077728360587,
        (7, 2): -0.0525756084128191,
        (7, 3): 0.068779985708525,
        (7, 4): -0.146937171125042,
        (7, 5): 0.113635799710859,
        (7, 6): -0.346290824830012,
        (7, 7): 0.303620041005904,
        (7, 8): -0.199174520212824,
        (7, 9): 0.114552984120296,
        (7, 10): -0.0532381287522677,
        (7, 11): 0.0517904540767088,
        (8, 0): 0.0203259967167556,
        (8, 1): -0.0256826119248349,
        (8, 2): 0.0277749850981131,
        (8, 3): -0.0351402135149769,
        (8, 4): 0.0685925655317263,
        (8, 5): -0.0572352443782531,
        (8, 6): 0.108283552025865,
        (8, 7): -0.199174520212824,
        (8, 8): 0.689553312888288,
        (8, 9): -0.373142162336678,
        (8, 10): 0.10237370314646,
        (8, 11): -0.107709400425106,
        (9, 0): -0.0275377468671827,
        (9, 1): 0.0333219425519274,
        (9, 2): -0.0371363305270252,
        (9, 3): 0.0435247904047193,
        (9, 4): -0.0890076598318992,
        (9, 5): 0.0632405366018826,
        (9, 6): -0.13356906288566,
        (9, 7): 0.114552984120296,
        (9, 8): -0.373142162336678,
        (9, 9): 0.296840045124218,
        (9, 10): -0.137610588198593,
        (9, 11): 0.110816804541974,
        (10, 0): 0.0154459653416028,
        (10, 1): -0.0178401278243851,
        (10, 2): 0.0207197497937901,
        (10, 3): -0.0224463805679564,
        (10, 4): 0.0461514107515209,
        (10, 5): -0.0330514824586447,
        (10, 6): 0.0665814977597425,
        (10, 7): -0.0532381287522677,
        (10, 8): 0.10237370314646,
        (10, 9): -0.137610588198593,
        (10, 10): 0.309928908881641,
        (10, 11): -0.421728143640927,
        (11, 0): -0.0157191000551504,
        (11, 1): 0.0186595479705245,
        (11, 2): -0.0209779658795406,
        (11, 3): 0.0237387702508952,
        (11, 4): -0.0477428675615197,
        (11, 5): 0.0334449788720193,
        (11, 6): -0.066080213271577,
        (11, 7): 0.0517904540767088,
        (11, 8): -0.107709400425106,
        (11, 9): 0.110816804541974,
        (11, 10): -0.421728143640927,
        (11, 11): 0.703171580607587,
    },
    periodic_bc: {
        (0, 0): 0.751970534661746,
        (0, 1): -0.236707243119345,
        (0, 2): 0.137547206113695,
        (0, 3): -0.1040797023312,
        (0, 4): 0.0754002612356565,
        (0, 5): -0.0703476956346235,
        (0, 6): 0.0705336897112939,
        (0, 7): -0.0689946405134317,
        (0, 8): 0.0713172226772661,
        (0, 9): -0.108328176770239,
        (0, 10): 0.147578066216467,
        (0, 11): -0.255219584725692,
        (1, 0): -0.236707243119345,
        (1, 1): 0.485094183892028,
        (1, 2): -0.377145944163698,
        (1, 3): 0.135669064979232,
        (1, 4): -0.0990781261905124,
        (1, 5): 0.0806447621714639,
        (1, 6): -0.0881586121175788,
        (1, 7): 0.0682511202227959,
        (1, 8): -0.0623435422086656,
        (1, 9): 0.0704928171089095,
        (1, 10): -0.0958036733792964,
        (1, 11): 0.110660640080166,
        (2, 0): 0.137547206113695,
        (2, 1): -0.377145944163698,
        (2, 2): 0.51387903277613,
        (2, 3): -0.232147139946612,
        (2, 4): 0.115269516240226,
        (2, 5): -0.0906760299912435,
        (2, 6): 0.0815474629836489,
        (2, 7): -0.0675013774015044,
        (2, 8): 0.0607593825487087,
        (2, 9): -0.0754450829312008,
        (2, 10): 0.0924020944038563,
        (2, 11): -0.102228823699145,
        (3, 0): -0.1040797023312,
        (3, 1): 0.135669064979232,
        (3, 2): -0.232147139946612,
        (3, 3): 0.225295503923788,
        (3, 4): -0.240239221381729,
        (3, 5): 0.123850250199894,
        (3, 6): -0.126328662058452,
        (3, 7): 0.0827807090585064,
        (3, 8): -0.0673826019482099,
        (3, 9): 0.0630104936793127,
        (3, 10): -0.0750093986615943,
        (3, 11): 0.0711928141642749,
        (4, 0): 0.0754002612356565,
        (4, 1): -0.0990781261905124,
        (4, 2): 0.115269516240226,
        (4, 3): -0.240239221381729,
        (4, 4): 0.516042987433842,
        (4, 5): -0.348754526490564,
        (4, 6): 0.173753140324495,
        (4, 7): -0.130377171992866,
        (4, 8): 0.0773722643654037,
        (4, 9): -0.0770493270005411,
        (4, 10): 0.0675903987731788,
        (4, 11): -0.0732122306357085,
        (5, 0): -0.0703476956346235,
        (5, 1): 0.0806447621714639,
        (5, 2): -0.0906760299912435,
        (5, 3): 0.123850250199894,
        (5, 4): -0.348754526490564,
        (5, 5): 0.567019907241631,
        (5, 6): -0.283207519112753,
        (5, 7): 0.114471020257401,
        (5, 8): -0.080214753433728,
        (5, 9): 0.065126437244307,
        (5, 10): -0.0656072861880371,
        (5, 11): 0.0597662971832623,
        (6, 0): 0.0705336897112939,
        (6, 1): -0.0881586121175788,
        (6, 2): 0.0815474629836489,
        (6, 3): -0.126328662058452,
        (6, 4): 0.173753140324495,
        (6, 5): -0.283207519112753,
        (6, 6): 0.607468173924469,
        (6, 7): -0.292093227075039,
        (6, 8): 0.105875571659179,
        (6, 9): -0.102090452738707,
        (6, 10): 0.0767630836362514,
        (6, 11): -0.078046483501324,
        (7, 0): -0.0689946405134318,
        (7, 1): 0.068251120222796,
        (7, 2): -0.0675013774015044,
        (7, 3): 0.0827807090585064,
        (7, 4): -0.130377171992866,
        (7, 5): 0.114471020257401,
        (7, 6): -0.292093227075039,
        (7, 7): 0.268971970495275,
        (7, 8): -0.245172192343923,
        (7, 9): 0.103683994325965,
        (7, 10): -0.0832897156677408,
        (7, 11): 0.0689294038267282,
        (8, 0): 0.0713172226772661,
        (8, 1): -0.0623435422086656,
        (8, 2): 0.0607593825487086,
        (8, 3): -0.0673826019482099,
        (8, 4): 0.0773722643654037,
        (8, 5): -0.080214753433728,
        (8, 6): 0.105875571659179,
        (8, 7): -0.245172192343923,
        (8, 8): 0.759467977530644,
        (8, 9): -0.284715231600668,
        (8, 10): 0.102943968333094,
        (8, 11): -0.10173422795094,
        (9, 0): -0.108328176770239,
        (9, 1): 0.0704928171089095,
        (9, 2): -0.0754450829312008,
        (9, 3): 0.0630104936793127,
        (9, 4): -0.0770493270005412,
        (9, 5): 0.0651264372443071,
        (9, 6): -0.102090452738707,
        (9, 7): 0.103683994325965,
        (9, 8): -0.284715231600668,
        (9, 9): 0.263497050408715,
        (9, 10): -0.244595812065143,
        (9, 11): 0.130997075137417,
        (10, 0): 0.147578066216467,
        (10, 1): -0.0958036733792964,
        (10, 2): 0.0924020944038563,
        (10, 3): -0.0750093986615943,
        (10, 4): 0.0675903987731788,
        (10, 5): -0.0656072861880371,
        (10, 6): 0.0767630836362514,
        (10, 7): -0.0832897156677407,
        (10, 8): 0.102943968333094,
        (10, 9): -0.244595812065143,
        (10, 10): 0.557555049427856,
        (10, 11): -0.364990495818253,
        (11, 0): -0.255219584725692,
        (11, 1): 0.110660640080166,
        (11, 2): -0.102228823699145,
        (11, 3): 0.071192814164275,
        (11, 4): -0.0732122306357085,
        (11, 5): 0.0597662971832623,
        (11, 6): -0.078046483501324,
        (11, 7): 0.0689294038267282,
        (11, 8): -0.10173422795094,
        (11, 9): 0.130997075137417,
        (11, 10): -0.364990495818253,
        (11, 11): 0.483737628283924,
    },
}

threshold = {
    open_bc: 1e-10,
    periodic_bc: 1e-10,
}

if __name__ == "__main__":
    import numpy as np
    np.set_printoptions(precision=10, suppress=True, threshold=10000, linewidth=300)

    L = 12
    hz_list = [-0.9994218963834927, -0.49906680067568954, 0.3714572638372098, 0.9629810631305735, 0.19369581339829733, -0.7411831242535816, -0.061683656841222456, 0.30784629029574884, -0.42077926330644844, 0.25473615736727395, 0.12683294253359123, -0.6640580830314939, 0.8068119905428868, 0.406662072822632, -0.9426452464446562, 0.20570260103193005, 0.05981505144670485, -0.7713553110794531, -0.21221662439093048, -0.47697716370894505]
    hz = lambda i: hz_list[i]

    for boundary_condition in (open_bc, periodic_bc):
        model = HeisenbergXXZChain(J=1., Jz=1., hz=hz, boundary_condition=boundary_condition)

        measurements = ([((i, "Sz"),) for i in range(L)] +
                        [((i, "Sz"), (j, "Sz")) for i in range(L) for j in range(L)] +
                        [((i, "Sp"), (j, "Sm")) for i in range(L) for j in range(L)])

        measurements_results = finite_system_algorithm(model, L=L, m_warmup=50, m_sweep_list=[50, 100, 200, 200], target_sector=0, measurements=measurements)

        measurements_map = dict(zip(measurements, measurements_results))

        # FIXME: compare also energy

        for site1, expected_value in expected_Sz[boundary_condition].items():
            actual_value = measurements_map[(site1, "Sz"),]
            diff = actual_value - expected_value
            assert abs(diff) < threshold[boundary_condition]
            print(diff, actual_value, expected_value)

        for (site1, site2), expected_value in expected_Sz_Sz[boundary_condition].items():
            actual_value = measurements_map[(site1, "Sz"), (site2, "Sz")]
            diff = actual_value - expected_value
            assert abs(diff) < threshold[boundary_condition]
            print(diff, actual_value, expected_value)

        for (site1, site2), expected_value in expected_Sp_Sm[boundary_condition].items():
            actual_value = measurements_map[(site1, "Sp"), (site2, "Sm")]
            diff = actual_value - expected_value
            assert abs(diff) < threshold[boundary_condition]
            print(diff, actual_value, expected_value)
