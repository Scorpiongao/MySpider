from singer import Singer
from singer_id import SingerId
from config import *
import pymongo

class SongId():
    def __init__(self):
        pass


    def get_song_id(self):
        singer_id = SingerId(GET_SINGER_URL)
        for artist in singer_id.get_json():
            id = artist['id']
            singername = artist['name']

            singer = Singer(id, singername)
            html = singer.request(singer.get_songs_url())
            songslist = singer.parse_songs_html(html)
            for song in songslist:
                song_id = song.get('href').split('=')[1]
                song = song.get('name')
                yield {
                    'singerId':id,
                    'singername':singername ,
                    'song_id' :song_id,
                    'song':song
                }


class   MvId():
    def __init__(self):
        pass


    def get_mv_id(self):
        client=pymongo .MongoClient (MONGO_URL ,connect= False )
        db=client [MONGO_DB ]
        singer_id = SingerId(GET_SINGER_URL)
        for artist in singer_id.get_json():
            id = artist['id']
            singername = artist['name']
            if db[MONGO_TABLE2].find_one({'id':id}):
                singer_mvs=db[MONGO_TABLE2 ].find_one({'id':id}).get('singer_mvs')
                if len(singer_mvs )>0:
                    for mvs in singer_mvs :
                        # print('mvs',mvs)
                        if len(mvs)>0:
                            for mv in mvs:
                                if mv:
                                # print('mv: ',mv)
                                    song=mv.get('mv')
                                    mv_id=mv['href'].split('=')[1]
                                    yield {
                                        'singerId':id,
                                        'singername':singername ,
                                        'mv_id' :mv_id,
                                        'song':song
                                    }