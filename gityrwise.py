import os
import json
import requests
import httplib
import filesequence

def Run_Fetch():
    headers = dict(Authorization='token %s' % os.environ['GITHUB_TOKEN'])

    filenames = filesequence.interpolator('data/repositories-%02d.json', xrange(1, 100))

    with filesequence.open(filenames, 50000000, flag='a+') as output:
        entries = [dict(id=0)] + [json.loads(line) for line in output.tail()]

        since = entries[-1]['id']

        while True:
            try:
                r = requests.get('https://api.github.com/repositories', headers=headers, params=dict(since=since))
            except httplib.IncompleteRead, exc:
                print exc
                print 'continuing'
                continue

            entries = r.json()

            remaining = r.headers.get('x-ratelimit-remaining', '0')
            limit = r.headers.get('x-ratelimit-limit', '0')
            print '%d since %d (%s/%s)' % (len(entries), since, remaining, limit)
            if 'message' in entries:
                print 'Error:', entries['message'], r
                continue

            if len(entries) < 10:
                print 'Too few entries'
                print entries

            for entry in entries:
                owner = entry['owner'] or {'login': 'N/A', 'id': 'N/A', 'type': 'N/A'}
                try:
                    s = requests.get('https://api.github.com/repos/'+owner['login']+'/'+entry['name']+'/stats/participation', headers=headers, params=dict(since=since))
                except httplib.IncompleteRead, exc:
                    print exc
                    print 'continuing'
                    continue
                stats=s.json()
                
                if 'message' in entries:
                    print 'Error:', entries['message'], r
                    continue

                if stats is not None:
                    if 'owner' in stats and len(stats['owner']) is not 0:
                        try:
                            f = requests.get('https://api.github.com/users/'+owner['login'], headers=headers, params=dict(since=since))
                        except httplib.IncompleteRead, exc:
                            print exc
                            print 'continuing'
                            continue
                        user=f.json()
                        repo = {
                            'id': entry['id'],
                            'name': entry['name'],
                            'full_name': entry['full_name'],
                            'description': entry['description'],
                            #'fork': entry['fork'],
                            'owner': owner['login'],
                            'owner_id': owner['id'],
                            'owner_type': owner['type'],
                            'followers':user['followers'],
                            'First_Month':stats['owner'][0]+stats['owner'][1]+stats['owner'][2]+stats['owner'][3]+stats['owner'][4],
                            'Second_Month':stats['owner'][5]+stats['owner'][6]+stats['owner'][7]+stats['owner'][8],
                            'Third_Month':stats['owner'][9]+stats['owner'][10]+stats['owner'][11]+stats['owner'][12]+stats['owner'][13],
                            'Fourth_Month':stats['owner'][14]+stats['owner'][15]+stats['owner'][16]+stats['owner'][17],
                            'Fifth_Month':stats['owner'][18]+stats['owner'][19]+stats['owner'][20]+stats['owner'][21]+stats['owner'][22],
                            'Sixth_Month':stats['owner'][23]+stats['owner'][24]+stats['owner'][25]+stats['owner'][26],
                            'Seventh_Month':stats['owner'][27]+stats['owner'][28]+stats['owner'][29]+stats['owner'][30]+stats['owner'][31],
                            'Eighth_Month':stats['owner'][32]+stats['owner'][33]+stats['owner'][34]+stats['owner'][35],
                            'Ninth_Month':stats['owner'][36]+stats['owner'][37]+stats['owner'][38]+stats['owner'][39],
                            'Tenth_Month':stats['owner'][40]+stats['owner'][41]+stats['owner'][42]+stats['owner'][43],
                            'Eleventh_Month':stats['owner'][44]+stats['owner'][45]+stats['owner'][46]+stats['owner'][47],
                            'Twelveth_Month':stats['owner'][48]+stats['owner'][49]+stats['owner'][50]+stats['owner'][51],
                            }
                    else:
                        continue
                else:
                    continue
                print "writing repo id:",entry['id']
                output.write('%s\n' % json.dumps(repo))

            since = entries[-1]['id']