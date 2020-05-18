from django.db import models


class Ttdphw016100(models.Model):
    t_unid = models.AutoField(primary_key=True)
    t_orno = models.CharField(max_length=9)
    t_corno = models.CharField(max_length=35)
    t_cornodt = models.DateTimeField()
    t_cremk = models.CharField(max_length=30)
    t_tandc = models.IntegerField()
    t_tncdt = models.DateTimeField()
    t_tncrem = models.CharField(max_length=30)
    t_aprv = models.IntegerField()
    t_cprj = models.CharField(max_length=9)
    t_apdt = models.DateTimeField()
    t_arem = models.CharField(max_length=30)
    t_puin = models.IntegerField()
    t_porno = models.IntegerField()
    t_mfgdraw = models.IntegerField()
    t_prdorno = models.IntegerField()
    t_test = models.IntegerField()
    t_testdate = models.DateTimeField()
    t_pack = models.IntegerField()
    t_shpm = models.IntegerField()
    t_pono = models.IntegerField()
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.
    t_cnama = models.CharField(max_length=35)
    t_comp = models.IntegerField()
    t_divs = models.CharField(max_length=25)
    t_idsca = models.CharField(max_length=30)
    t_invto = models.CharField(max_length=3)
    t_item = models.CharField(max_length=47)
    t_ldfl = models.IntegerField()
    t_mfgcdate = models.DateTimeField()
    t_mfgcomp = models.IntegerField()
    t_mfgdrwdt = models.DateTimeField()
    t_packdate = models.DateTimeField()
    t_podate = models.DateTimeField()
    t_prdorndt = models.DateTimeField()
    t_puindate = models.DateTimeField()
    t_rvno = models.IntegerField()
    t_shpmdate = models.DateTimeField()
    t_shpto = models.CharField(max_length=1)
    t_sqnb = models.IntegerField()
    t_submit = models.IntegerField()
    t_submitdt = models.DateTimeField()
    t_zone = models.CharField(max_length=50)
    t_odat = models.DateTimeField()
    t_rqno = models.CharField(max_length=9)
    t_rqnostat = models.IntegerField()
    t_sub = models.CharField(max_length=9)
    t_pnum = models.CharField(max_length=9)
    t_prdnum = models.CharField(max_length=9)
    t_reldt = models.DateTimeField()
    t_sldt = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'ttdphw016100'


class Ttdphw016200(models.Model):
    t_unid = models.AutoField(primary_key=True)
    t_orno = models.CharField(max_length=9)
    t_corno = models.CharField(max_length=35)
    t_cornodt = models.DateTimeField()
    t_cremk = models.CharField(max_length=30)
    t_tandc = models.IntegerField()
    t_tncdt = models.DateTimeField()
    t_tncrem = models.CharField(max_length=30)
    t_aprv = models.IntegerField()
    t_cprj = models.CharField(max_length=9)
    t_apdt = models.DateTimeField()
    t_arem = models.CharField(max_length=30)
    t_puin = models.IntegerField()
    t_porno = models.IntegerField()
    t_mfgdraw = models.IntegerField()
    t_prdorno = models.IntegerField()
    t_test = models.IntegerField()
    t_testdate = models.DateTimeField()
    t_pack = models.IntegerField()
    t_shpm = models.IntegerField()
    t_pono = models.IntegerField()
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.
    t_cnama = models.CharField(max_length=35)
    t_comp = models.IntegerField()
    t_divs = models.CharField(max_length=25)
    t_idsca = models.CharField(max_length=30)
    t_invto = models.CharField(max_length=3)
    t_item = models.CharField(max_length=47)
    t_ldfl = models.IntegerField()
    t_mfgcdate = models.DateTimeField()
    t_mfgcomp = models.IntegerField()
    t_mfgdrwdt = models.DateTimeField()
    t_packdate = models.DateTimeField()
    t_podate = models.DateTimeField()
    t_prdorndt = models.DateTimeField()
    t_puindate = models.DateTimeField()
    t_rvno = models.IntegerField()
    t_shpmdate = models.DateTimeField()
    t_shpto = models.CharField(max_length=1)
    t_sqnb = models.IntegerField()
    t_submit = models.IntegerField()
    t_submitdt = models.DateTimeField()
    t_zone = models.CharField(max_length=50)
    t_odat = models.DateTimeField()
    t_rqno = models.CharField(max_length=9)
    t_rqnostat = models.IntegerField()
    t_sub = models.CharField(max_length=9)
    t_pnum = models.CharField(max_length=9)
    t_prdnum = models.CharField(max_length=9)
    t_reldt = models.DateTimeField()
    t_sldt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ttdphw016200'


class Ttdphw016300(models.Model):
    t_unid = models.AutoField(primary_key=True)
    t_orno = models.CharField(max_length=9)
    t_corno = models.CharField(max_length=35)
    t_cornodt = models.DateTimeField()
    t_cremk = models.CharField(max_length=30)
    t_tandc = models.IntegerField()
    t_tncdt = models.DateTimeField()
    t_tncrem = models.CharField(max_length=30)
    t_aprv = models.IntegerField()
    t_cprj = models.CharField(max_length=9)
    t_apdt = models.DateTimeField()
    t_arem = models.CharField(max_length=30)
    t_puin = models.IntegerField()
    t_porno = models.IntegerField()
    t_mfgdraw = models.IntegerField()
    t_prdorno = models.IntegerField()
    t_test = models.IntegerField()
    t_testdate = models.DateTimeField()
    t_pack = models.IntegerField()
    t_shpm = models.IntegerField()
    t_pono = models.IntegerField()
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.
    t_cnama = models.CharField(max_length=35)
    t_comp = models.IntegerField()
    t_divs = models.CharField(max_length=25)
    t_idsca = models.CharField(max_length=30)
    t_invto = models.CharField(max_length=3)
    t_item = models.CharField(max_length=47)
    t_ldfl = models.IntegerField()
    t_mfgcdate = models.DateTimeField()
    t_mfgcomp = models.IntegerField()
    t_mfgdrwdt = models.DateTimeField()
    t_packdate = models.DateTimeField()
    t_podate = models.DateTimeField()
    t_prdorndt = models.DateTimeField()
    t_puindate = models.DateTimeField()
    t_rvno = models.IntegerField()
    t_shpmdate = models.DateTimeField()
    t_shpto = models.CharField(max_length=1)
    t_sqnb = models.IntegerField()
    t_submit = models.IntegerField()
    t_submitdt = models.DateTimeField()
    t_zone = models.CharField(max_length=50)
    t_odat = models.DateTimeField()
    t_rqno = models.CharField(max_length=9)
    t_rqnostat = models.IntegerField()
    t_sub = models.CharField(max_length=9)
    t_pnum = models.CharField(max_length=9)
    t_prdnum = models.CharField(max_length=9)
    t_reldt = models.DateTimeField()
    t_sldt = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'ttdphw016300'


class BryUser(models.Model):
    t_unid = models.AutoField(primary_key=True)
    t_usr = models.CharField(max_length=15)
    t_comp = models.IntegerField()
    t_mbno = models.CharField(max_length=12)
    t_cofc = models.CharField(max_length=6)
    t_autk = models.CharField(max_length=15)
    t_dtyp = models.CharField(max_length=10)
    t_ustat = models.IntegerField()
    t_isatuc = models.IntegerField()
    t_ispass = models.IntegerField()
    t_pass = models.CharField(max_length=256)
    t_passdate = models.DateTimeField()
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.
    t_nama = models.CharField(max_length=35)
    t_deviceid = models.CharField(max_length=50)
    # t_company = models.CharField(max_length=50)
    # t_zone = models.CharField(max_length=5)
    # t_diva = models.CharField(max_length=5)
    t_otp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ttdphw017100'


class Ttdphw018100(models.Model):
    t_unid = models.IntegerField()
    t_orno = models.CharField(max_length=9)
    t_pono = models.IntegerField()
    t_sqnb = models.IntegerField()
    t_rvno = models.IntegerField()
    t_sdate = models.DateTimeField()
    t_remk = models.CharField(max_length=50)
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw018100'


class Ttdphw018200(models.Model):
    t_unid = models.IntegerField()
    t_orno = models.CharField(max_length=9)
    t_pono = models.IntegerField()
    t_sqnb = models.IntegerField()
    t_rvno = models.IntegerField()
    t_sdate = models.DateTimeField()
    t_remk = models.CharField(max_length=50)
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw018200'


class Ttdphw018300(models.Model):
    t_unid = models.IntegerField()
    t_orno = models.CharField(max_length=9)
    t_pono = models.IntegerField()
    t_sqnb = models.IntegerField()
    t_rvno = models.IntegerField()
    t_sdate = models.DateTimeField()
    t_remk = models.CharField(max_length=50)
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw018300'


class Ttdphw019100(models.Model):
    t_unid = models.AutoField(primary_key=True)
    t_user = models.CharField(max_length=15)
    t_zone = models.CharField(max_length=15)
    t_div = models.CharField(max_length=25)
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw019100'


class Ttdphw020100(models.Model):
    t_ncmp = models.AutoField(primary_key=True)
    t_div = models.CharField(max_length=25)
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.
    t_ornoch = models.CharField(max_length=1)
    t_unid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ttdphw020100'


class Ttdphw021100(models.Model):
    t_unid = models.IntegerField()
    t_zone = models.CharField(max_length=1)
    t_dsca = models.CharField(max_length=15)
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw021100'


class Ttdphw022100(models.Model):
    t_unid = models.IntegerField()
    t_mlcd = models.CharField(max_length=15)
    t_mdsca = models.CharField(max_length=30)
    t_linkf = models.CharField(max_length=50)
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw022100'


class Ttdphw023100(models.Model):
    t_ncmp = models.IntegerField()
    t_comp = models.IntegerField()
    t_mlcd = models.CharField(max_length=15)
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.
    t_unid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ttdphw023100'

class Ttdphw024100(models.Model):
    t_unid = models.AutoField(primary_key=True)
    t_orno = models.CharField(max_length=9)
    t_pono = models.IntegerField()
    t_seqn = models.IntegerField()
    t_strdt = models.DateTimeField()
    t_atrdt = models.DateTimeField()
    t_rtrdt = models.DateTimeField()
    t_ptrdt = models.DateTimeField()
    t_pornotrd = models.DateTimeField()
    t_mfgtrdt = models.DateTimeField()
    t_prdtrdt = models.DateTimeField()
    t_mctrdt = models.DateTimeField()
    t_testtrdt = models.DateTimeField()
    t_packtrdt = models.DateTimeField()
    t_shptrdt = models.DateTimeField()
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw024100'


class Ttdphw024200(models.Model):
    t_unid = models.AutoField(primary_key=True)
    t_orno = models.CharField(max_length=9)
    t_pono = models.IntegerField()
    t_seqn = models.IntegerField()
    t_strdt = models.DateTimeField()
    t_atrdt = models.DateTimeField()
    t_rtrdt = models.DateTimeField()
    t_ptrdt = models.DateTimeField()
    t_pornotrd = models.DateTimeField()
    t_mfgtrdt = models.DateTimeField()
    t_prdtrdt = models.DateTimeField()
    t_mctrdt = models.DateTimeField()
    t_testtrdt = models.DateTimeField()
    t_packtrdt = models.DateTimeField()
    t_shptrdt = models.DateTimeField()
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw024200'


class Ttdphw024300(models.Model):
    t_unid = models.AutoField(primary_key=True)
    t_orno = models.CharField(max_length=9)
    t_pono = models.IntegerField()
    t_seqn = models.IntegerField()
    t_strdt = models.DateTimeField()
    t_atrdt = models.DateTimeField()
    t_rtrdt = models.DateTimeField()
    t_ptrdt = models.DateTimeField()
    t_pornotrd = models.DateTimeField()
    t_mfgtrdt = models.DateTimeField()
    t_prdtrdt = models.DateTimeField()
    t_mctrdt = models.DateTimeField()
    t_testtrdt = models.DateTimeField()
    t_packtrdt = models.DateTimeField()
    t_shptrdt = models.DateTimeField()
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw024300'



class Ttdphw025100(models.Model):
    t_unid = models.AutoField(primary_key=True)
    t_orno = models.CharField(max_length=9)
    t_pono = models.IntegerField()
    t_sqnb = models.IntegerField()
    t_mlcd = models.CharField(max_length=15)
    t_mldsca = models.CharField(max_length=30)
    t_trdt = models.DateTimeField()
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw025100'


class Ttdphw025200(models.Model):
    t_unid = models.AutoField(primary_key=True)
    t_orno = models.CharField(max_length=9)
    t_pono = models.IntegerField()
    t_sqnb = models.IntegerField()
    t_mlcd = models.CharField(max_length=15)
    t_mldsca = models.CharField(max_length=30)
    t_trdt = models.DateTimeField()
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw025200'


class Ttdphw025300(models.Model):
    t_unid = models.AutoField(primary_key=True)
    t_orno = models.CharField(max_length=9)
    t_pono = models.IntegerField()
    t_sqnb = models.IntegerField()
    t_mlcd = models.CharField(max_length=15)
    t_mldsca = models.CharField(max_length=30)
    t_trdt = models.DateTimeField()
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw025300'



class Ttdphw026100(models.Model):
    t_unid =  models.AutoField(primary_key=True)
    t_usid = models.CharField(max_length=15)
    t_deviceid = models.CharField(max_length=50)
    t_datetime = models.DateTimeField()
    t_duration = models.CharField(max_length=50)
    t_actn = models.CharField(max_length=50)
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw026100'
