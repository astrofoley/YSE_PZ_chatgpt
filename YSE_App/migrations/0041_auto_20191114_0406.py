# Generated by Django 2.0.4 on 2019-11-14 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('YSE_App', '0040_auto_20191110_0247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyobservationtask',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='surveyobservationtask',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='surveyobservationtask',
            name='requested_photometric_band',
        ),
        migrations.RemoveField(
            model_name='surveyobservationtask',
            name='status',
        ),
        migrations.RemoveField(
            model_name='surveyobservationtask',
            name='survey_field',
        ),
        migrations.RemoveField(
            model_name='surveyfield',
            name='first_mjd',
        ),
        migrations.RemoveField(
            model_name='surveyfield',
            name='last_mjd',
        ),
        migrations.RemoveField(
            model_name='surveyobservation',
            name='survey_observation_task',
        ),
        migrations.AddField(
            model_name='surveyobservation',
            name='mjd_requested',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='surveyobservation',
            name='survey_field',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='YSE_App.SurveyField'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SurveyObservationTask',
        ),
    ]
