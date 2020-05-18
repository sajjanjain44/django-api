from django.db import models


# Create your models here.

class BryUser(models.Model):
    t_usr = models.CharField(max_length=15)
    t_mbno = models.CharField(max_length=10)
    t_zone = models.CharField(max_length=3)
    t_diva = models.CharField(max_length=3)
    t_cofc = models.CharField(max_length=6)
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.
    t_autk = models.CharField(max_length=25)
    t_dtyp = models.CharField(max_length=10)
    t_isatuc = models.IntegerField()
    t_ustat = models.IntegerField()
    t_ispass = models.IntegerField()
    t_pass = models.CharField(max_length=25)
    t_passdate = models.DateTimeField()
    t_id = models.AutoField(primary_key=True)
    t_device_id = models.CharField(max_length=25)
    t_company = models.CharField(max_length=10)
    class Meta:
        managed = False
        db_table = 'ttdphw017100'

    def __str__(self):
        return self.t_usr


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
    # userByZone = models.ForeignKey(BryUser,on_delete=models.CASCADE,to_field='t_zone')

    class Meta:
        managed = False
        db_table = 'ttdphw016100'


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



class Ttdphw023100(models.Model):
    t_unid = models.AutoField(primary_key=True)
    t_ncmp = models.IntegerField()
    t_comp = models.IntegerField()
    t_mlcd = models.CharField(max_length=10)
    t_refcntd = models.IntegerField(db_column='t_Refcntd')  # Field name made lowercase.
    t_refcntu = models.IntegerField(db_column='t_Refcntu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ttdphw023100'


class Ttdphw022100(models.Model):
    t_unid = models.AutoField(primary_key=True)
    t_mlcd = models.CharField(max_length=15)
    t_mdsca = models.CharField(max_length=30)
    t_linked_field = models.CharField(max_length=10)
    class Meta:
        managed = False
        db_table = 'ttdphw022100'