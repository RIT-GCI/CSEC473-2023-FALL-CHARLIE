dirs = ['/var/log', '/var/cache', '/home/navy', '/home',
        ]

fnames = ['flag.txt', 'ls', 'init.log', 'a.a', 'a',
          ]

alpha = [*(chr(a) for a in range(97, 123))] + [*(chr(a) for a in range(65, 91))]
alpha_num = alpha + [*(chr(a) for a in range(0x30, 0x3a))]
all_chrs = [*(chr(a) for a in range(33, 127))]

fake_prefixes = ['fake', 'blueteam', 'bteam', 'merica', 'prussia', 'bt', 'bert', 'ifOnly', 'getbetterregex',
                 'orangeTeam', 'China', 'purpleteam', 'red-ish', 'reallyredlookingorange', 'notred', 'fakeredteam',
                 'almost', 'maroonteam', 'fatherPrussia',
                 ]
fake_flags = ['fake', 'notreal', 'f@k3', 'n0tr34l', 'hahahanotreal', 'not_a_real_flag', 'fakeflag', 'f4kefl4g',
              'tryagain', 'thisaintitchief', 'not_real_try_again', 'sham flag', 'oops, not this one',
              'not_real', 'n_o_t_r_e_a_l', 'whoopsies this flag is the opposite of real', 'so close! but no.',
              'faaaaaaaakkeeee', "this flag is so fake it's sad", 'imposter flag is sus ඞඞඞඞඞ (not real)',
              'pretendFlag', 'thisFlagIsAForgery', 'imitationflag', 'next time try regex? this one is fake',
              'how many synonyms for fake does your regex account for?', 'falseFlag',
              ]
