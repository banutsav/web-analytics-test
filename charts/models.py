# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EblityAttendanceTable(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    check_in = models.TimeField(blank=True, null=True)
    check_out = models.TimeField(blank=True, null=True)
    tutor_time = models.CharField(max_length=15)
    commitment = models.CharField(max_length=100)
    p_a = models.CharField(max_length=15)
    reason_for_absence = models.CharField(max_length=100)
    student_id = models.ForeignKey('EblityStudentTable', models.DO_NOTHING)
    slot = models.CharField(max_length=15)
    student_name = models.CharField(max_length=20)
    grade = models.IntegerField(blank=True, null=True)
    com_status = models.CharField(max_length=15)
    date = models.DateField()
    center = models.IntegerField()
    subtopic_name = models.CharField(max_length=100)
    subtopic_progress = models.IntegerField(blank=True, null=True)
    topic_name = models.CharField(max_length=100)
    topic_progress = models.IntegerField(blank=True, null=True)
    updated = models.IntegerField()
    rem_topic_count = models.IntegerField()
    rem_subtopic_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eblity_attendance_table'


class EblityCenter(models.Model):
    center_code = models.IntegerField(primary_key=True)
    center_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'eblity_center'


class EblityCurrentTopic(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    student_id = models.IntegerField()
    topic_id = models.IntegerField()
    topic_name = models.CharField(max_length=50)
    subtopic_id = models.IntegerField()
    subtopic_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'eblity_current_topic'


class EblityGrade(models.Model):
    grade_code = models.IntegerField(primary_key=True)
    grade_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'eblity_grade'


class EblityJourneyTemplate(models.Model):
    subtopic_id = models.IntegerField()
    journey_template_key = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=30)
    rating = models.FloatField(blank=True, null=True)
    time_spent = models.TimeField(blank=True, null=True)
    feedback = models.CharField(max_length=1000, blank=True, null=True)
    resource_id = models.ForeignKey('EblityResources', models.DO_NOTHING)
    topic_id = models.ForeignKey('EblityTopicTable', models.DO_NOTHING)
    student_id = models.ForeignKey('EblityStudentTable', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'eblity_journey_template'


class EblityLogTable(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    resource_type = models.CharField(max_length=25)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=15)
    subtopic_id = models.IntegerField(blank=True, null=True)
    topic_name = models.CharField(max_length=25)
    subtopic_name = models.CharField(max_length=25)
    resource_id = models.ForeignKey('EblityResources', models.DO_NOTHING)
    student_id = models.ForeignKey('EblityStudentTable', models.DO_NOTHING)
    topic_id = models.ForeignKey('EblityTopicTable', models.DO_NOTHING)
    tut_end_time = models.TimeField()
    tut_start_time = models.TimeField()
    tutor_time = models.FloatField()

    class Meta:
        managed = False
        db_table = 'eblity_log_table'


class EblityPlanTable(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    topic_name = models.CharField(max_length=100)
    weightage = models.CharField(max_length=15)
    sequence = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=15)
    hours = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=20)
    student_id = models.ForeignKey('EblityStudentTable', models.DO_NOTHING)
    topic_id = models.ForeignKey('EblityTopicTable', models.DO_NOTHING)
    topic_progress = models.IntegerField()
    subject_progress = models.IntegerField()
    subtopic_id = models.IntegerField(blank=True, null=True)
    subtopic_name = models.CharField(max_length=100)
    subtopic_progress = models.IntegerField()
    subtopic_status = models.CharField(max_length=15)
    topic_status = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'eblity_plan_table'


class EblityResources(models.Model):
    resource_id = models.IntegerField(primary_key=True)
    subtopic_id = models.IntegerField()
    resource_type = models.CharField(max_length=30)
    resource_link = models.CharField(max_length=200)
    tags = models.CharField(max_length=30)
    topic_id = models.ForeignKey('EblityTopicTable', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'eblity_resources'


class EblitySlot(models.Model):
    slot_code = models.IntegerField(primary_key=True)
    slot_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'eblity_slot'


class EblityStudentTable(models.Model):
    student_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    grade = models.IntegerField()
    parent_id = models.IntegerField()
    parent_email = models.CharField(max_length=20)
    status = models.CharField(max_length=15)
    slot = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    center = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eblity_student_table'


class EblitySubtopicTable(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    subtopic_id = models.IntegerField()
    subtopic_name = models.CharField(max_length=25)
    sequence = models.IntegerField(blank=True, null=True)
    max_minutes = models.FloatField(blank=True, null=True)
    topic_id = models.ForeignKey('EblityTopicTable', models.DO_NOTHING)
    grade = models.IntegerField(blank=True, null=True)
    mean_minutes = models.FloatField(blank=True, null=True)
    min_minutes = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eblity_subtopic_table'


class EblityTopicTable(models.Model):
    topic_id = models.IntegerField(primary_key=True)
    topic_name = models.CharField(max_length=100)
    weightage = models.CharField(max_length=15)
    grade = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=100)
    sequence = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=15)
    mean_minutes = models.FloatField(blank=True, null=True)
    max_minutes = models.FloatField(blank=True, null=True)
    pre_mid_term = models.CharField(max_length=15)
    mid_term = models.CharField(max_length=15)
    pre_final_term = models.CharField(max_length=15)
    final_term = models.CharField(max_length=15)
    min_minutes = models.FloatField(blank=True, null=True)
    hours = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eblity_topic_table'


class EblityUserprofileinfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    role_type = models.IntegerField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)
    grade = models.IntegerField()
    first_name_p = models.CharField(max_length=50)
    last_name_p = models.CharField(max_length=50)
    center_type = models.IntegerField()
    slot = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'eblity_userprofileinfo'


class LgData(models.Model):
    date = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    subtopic = models.TextField(blank=True, null=True)
    ld_type_id = models.TextField(db_column='LD_type_ID', blank=True, null=True)  # Field name made lowercase.
    lg_desc = models.TextField(db_column='LG_desc', blank=True, null=True)  # Field name made lowercase.
    lg_strength = models.FloatField(db_column='LG_strength', blank=True, null=True)  # Field name made lowercase.
    strong_or_weak = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lg_data'


class PerfTrail(models.Model):
    date = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    subject_progress = models.IntegerField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    topic_progress = models.IntegerField(blank=True, null=True)
    subtopic = models.TextField(blank=True, null=True)
    subtopic_progress = models.IntegerField(blank=True, null=True)
    sub_sub_topic = models.TextField(blank=True, null=True)
    blto = models.TextField(db_column='BLTO', blank=True, null=True)  # Field name made lowercase.
    difficulty_level = models.TextField(blank=True, null=True)
    timespent = models.IntegerField(blank=True, null=True)
    attempts = models.IntegerField(blank=True, null=True)
    errors = models.IntegerField(blank=True, null=True)
    is_solved = models.NullBooleanField()
    fundaas = models.IntegerField(blank=True, null=True)
    bonus_fundaas = models.TextField(blank=True, null=True)
    lg_type_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perf_trail'
