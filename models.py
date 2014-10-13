from google.appengine.ext import ndb

class ProfileImage(ndb.Model):
	file_name = ndb.StringProperty()
	image_file = ndb.BlobProperty()

class User(ndb.Model):
  name = ndb.StringProperty()
  datetime_created = ndb.DateTimeProperty(auto_now_add=True)
  num_post = ndb.IntegerProperty()
  num_follower = ndb.IntegerProperty()
  num_following = ndb.IntegerProperty()
  total_reply = ndb.IntegerProperty()
  total_reply_to = ndb.IntegerProperty()
  total_good_post = ndb.IntegerProperty()
  total_neutral_post = ndb.IntegerProperty()
  about = ndb.StringProperty()
  profile_pic = ndb.KeyProperty(kind=ProfileImage)
  private = ndb.BooleanProperty(default=False)
  ip = ndb.StringProperty()
  geo_location = ndb.StringProperty()

class Post(ndb.Model):
	subject = ndb.StringProperty()
	content = ndb.StringProperty()
	view_count = ndb.IntegerProperty()
	user_pk = ndb.KeyProperty(kind=User)
	datetime_created = ndb.DateTimeProperty(auto_now_add=True)
	
	num_high_fives = ndb.IntegerProperty()
	num_low_fives = ndb.IntegerProperty()
	replies = ndb.KeyProperty(kind='Post', repeated=True)
	reply_tos = ndb.KeyProperty(kind='Post', repeated=True)
	post_type = ndb.StringProperty(required=True, choices=['good', 'bad', 'neutral'])
	ip = ndb.StringProperty()
	geo_location = ndb.StringProperty()

 class Image(ndb.Model):
 	post_pk = ndb.KeyProperty(kind=Post)
 	image_file = ndb.BlobProperty()
 	image_links = ndb.StringProperty(repeated=True)
 	user_pk = ndb.KeyProperty(kind=User)
 	description = ndb.StringProperty()

class Video(ndb.Model):
	post_pk = ndb.KeyProperty(kind=Post)
	video_file = ndb.BlobProperty()
	video_links = ndb.StringProperty(repeated=True)
	user_pk = ndb.KeyProperty(kind=User)
	description = ndb.StringProperty()