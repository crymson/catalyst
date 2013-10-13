class Generic:
	def __init__(self, myspec):
		self.settings = myspec

	def mount_safety_check(self):
		"""
		Make sure that no bind mounts exist in chrootdir (to use before
		cleaning the directory, to make sure we don't wipe the contents of
		a bind mount
		"""
        raise NotImplementedError

	def mount_all(self):
		"""do all bind mounts"""
        raise NotImplementedError

	def umount_all(self):
		"""unmount all bind mounts"""
        raise NotImplementedError
