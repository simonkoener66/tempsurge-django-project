import csv
import string
from datetime import datetime

from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import User
from django.db import IntegrityError

from agencies.models import StaffingAgency, Branch
from temps.models import Temp
from accounts.geo.models import Country, State, County, City
from tempsurge.utils.StringHelper import random_string


class Command(BaseCommand):
    def handle(self, *args, **options):
        csv_file_path = '%s/storage/temp/Platinum EmployeeView List.csv' % settings.BASE_DIR

        agency = StaffingAgency.objects.get(name='Tempsurge')

        with open(csv_file_path, 'rb') as csvfile:
            # temp_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            temp_reader = csv.DictReader(csvfile)

            print temp_reader

            i = 0
            active = 0
            inactive = 0

            for row in temp_reader:
                i += 1

                # Add a few for debugging
                # if i == 5:
                #     break

                print row

                # Ignore inactive temp and those without land or cell phone
                if row['Active'] == '0':
                    self.stdout.write('Ignoring inactive temp...')
                    inactive += 1
                    # print row
                    continue
                elif row['PhoneNumber'] == 'NULL' and row['CellPhone'] == 'NULL':

                    # self.stdout.write('Ignoring temp with no phone number...')
                    continue

                active += 1

                # print "active", str(active)
                # print "inactive", str(inactive)

                # continue

                # Create user account
                username = "%s.%s" % (null_to_none(row['FirstName']), null_to_none(row['LastName']))
                username = username.replace(' ', '').strip()

                while True:
                    try:
                        # print row['Email']
                        u = User.objects.create(
                            id=row['EmployeeId'],
                            username=username,
                            first_name=null_to_none(row['FirstName']),
                            last_name=null_to_none(row['LastName']),
                            email=null_to_none(row['Email'])
                        )

                        break
                    except IntegrityError, e:
                        print e
                        username += "-" + random_string(3, string.digits)


                # Get or create geo records

                ## Country
                country = Country.objects.get(name='United States')

                ## State
                if null_to_none(row['State']):
                    state = State.objects.get_or_create(name=null_to_none(row['State']), country=country, agency=agency)[0]
                else:
                    state = None

                ## TaxState
                if null_to_none(row['TaxState']):
                    tax_state = State.objects.get_or_create(name=null_to_none(row['TaxState']), country=country, agency=agency)[0]
                else:
                    tax_state = None

                ## County
                if null_to_none(row['County']):
                    county = County.objects.get_or_create(name=null_to_none(row['County']), state=state, agency=agency)[0]
                else:
                    county = None

                ## City
                if null_to_none(row['City']) and null_to_none(row['City']) != 'unknown':
                    city = City.objects.get_or_create(name=null_to_none(row['City']), country=country, agency=agency)[0]
                else:
                    city = None

                # Assign user profile to agency
                u.userprofile.initial = null_to_none(row['Initial'])
                u.userprofile.prefix = null_to_none(row['Prefix'])
                u.userprofile.nickname = null_to_none(row['NickName'])
                u.userprofile.address_line_1 = null_to_none(row['Address'])
                u.userprofile.address_line_2 = null_to_none(row['Address2'])
                u.userprofile.county = county
                u.userprofile.city = city
                u.userprofile.state = state
                u.userprofile.country = country
                u.userprofile.zip = null_to_none(row['Zip'])
                u.userprofile.phone = null_to_none(row['PhoneNumber'])
                u.userprofile.cell_phone = null_to_none(row['CellPhone'])

                u.userprofile.agency = agency
                u.userprofile.save()

                try:
                    InterviewedByRepName = User.objects.get(username=null_to_none(row['InterviewedByRepName']))
                except User.DoesNotExist:
                    InterviewedByRepName = None

                # Create temp profile
                t = Temp.objects.create(
                    SMS=null_to_none(row['SMS']),
                    rep=User.objects.get(username=null_to_none(row['RepName'])),
                    entered_by_rep=User.objects.get(username=null_to_none(row['EnteredByRepName'])),
                    InterviewedByRepName=InterviewedByRepName,
                    EmploymentCategory=null_to_none(row['EmploymentCategory']),
                    AIdent=null_to_none(row['AIdent']),
                    ssn=null_to_none(row['SSN']),
                    active=null_to_none(row['Active']),
                    assigned=null_to_none(row['Assigned']),
                    WashedStatus=null_to_none(row['WashedStatus']),
                    Burden=null_to_none(row['Burden']),
                    ActivationDate=excel_to_django_date(row['ActivationDate']),
                    DeActivationDate=excel_to_django_date(row['DeActivationDate']),
                    YTDEarnings=int_field(row['YTDEarnings']),
                    OtherAddress=null_to_none(row['OtherAddress']),
                    SecurityClearance=null_to_none(row['SecurityClearance']),
                    DrugTest=null_to_none(row['DrugTest']),
                    MaritalTaxStatusId=int_field(row['MaritalTaxStatusId']),
                    Birthday = null_to_none(row['Birthday']),
                    state_exemptions=int_field(row['StateExemptions']),
                    federal_exemptions=int_field(row['FederalExemptions']),
                    Dependents=int_field(row['Dependents']),
                    MailCheck=null_to_none(row['MailCheck']),
                    EmergencyContact=null_to_none(row['EmergencyContact']),
                    RightToWork=null_to_none(row['RightToWork']),
                    _18orOlder=null_to_none(row['_18orOlder']),
                    Smoker=null_to_none(row['Smoker']),
                    ResumeOnfile=null_to_none(row['ResumeOnfile']),
                    CarAvailable=null_to_none(row['CarAvailable']),
                    TransportationDetails=null_to_none(row['TransportationDetails']),
                    I9Submitted=null_to_none(row['I9Submitted']),
                    Education=null_to_none(row['Education']),
                    DrugTested=null_to_none(row['DrugTested']),
                    BackgroundChecked=null_to_none(row['BackgroundChecked']),
                    Convictions=null_to_none(row['Convictions']),
                    ECurrentAssignment=null_to_none(row['ECurrentAssignment']),
                    EExpEnd=null_to_none(row['EExpEnd']),
                    EPayRate=decimal_field(row['EPayRate']),
                    ELastPerf=null_to_none(row['ELastPerf']),
                    EPayrollNote=null_to_none(row['EPayrollNote']),
                    TicklerDate=excel_to_django_date(row['TicklerDate']),
                    Class=null_to_none(row['Class']),
                    last_message=null_to_none(row['LastMsg']),
                    LastDate=excel_to_django_date(row['LastDate']),
                    WComp=null_to_none(row['WComp']),
                    CheckPayDay=null_to_none(row['CheckPayDay']),
                    LocalTaxCode=null_to_none(row['LocalTaxCode']),
                    TaxModel=null_to_none(row['TaxModel']),
                    TaxInitialized=null_to_none(row['TaxInitialized']),
                    CheckDelivery=null_to_none(row['CheckDelivery']),
                    ElectronicPay=null_to_none(row['ElectronicPay']),
                    PayPeriods=int_field(row['PayPeriods']),
                    LastModified=excel_to_django_date(row['LastModified']),
                    LastModifiedBySrident=int_field(row['LastModifiedBySrident']),
                    OrientationGiven=excel_to_django_date(row['OrientationGiven']),
                    EndDateAssign=excel_to_django_date(row['EndDateAssign']),
                    StartDateAssign=excel_to_django_date(row['StartDateAssign']),
                    ESort=int_field(row['ESort']),
                    AnniversaryDate=excel_to_django_date(row['AnniversaryDate']),
                    EStatus=null_to_none(row['EStatus']),
                    ENote=null_to_none(row['ENote']),
                    ReferencesChecked=null_to_none(row['ReferencesChecked']),
                    DrugAlcPolicy=null_to_none(row['DrugAlcPolicy']),
                    HarassmentPolicy=null_to_none(row['HarassmentPolicy']),
                    DMVCheck=null_to_none(row['DMVCheck']),
                    ReferencesClear=null_to_none(row['ReferencesClear']),
                    AlienRegistration=null_to_none(row['AlienRegistration']),
                    AdditionalWH=null_to_none(row['AdditionalWH']),
                    TaxExempt=null_to_none(row['TaxExempt']),
                    EMiscDate1=excel_to_django_date(row['EMiscDate1']),
                    InterviewedBySrident=int_field(row['InterviewedBySrident']),
                    DateRefCheck=excel_to_django_date(row['DateRefCheck']),
                    DateBCheck=excel_to_django_date(row['DateBCheck']),
                    DateDTest=excel_to_django_date(row['DateDTest']),
                    I9Date=excel_to_django_date(row['I9Date']),
                    DLState=null_to_none(row['DLState']),
                    DLNumber=null_to_none(row['DLNumber']),
                    DLClass=null_to_none(row['DLClass']),
                    SafetyCert=null_to_none(row['SafetyCert']),
                    DLExpire=excel_to_django_date(row['DLExpire']),
                    CountyJuris=null_to_none(row['CountyJuris']),
                    CityJuris=null_to_none(row['CityJuris']),
                    SchoolJuris=null_to_none(row['SchoolJuris']),
                    LocalJuris=null_to_none(row['LocalJuris']),
                    PrAlert=null_to_none(row['PrAlert']),
                    AltBranchName=null_to_none(row['AltBranchName']),
                    AltENum=null_to_none(row['AltENum']),
                    ChangeMailToTo=null_to_none(row['ChangeMailToTo']),
                    TaxState=tax_state,
                    LastBBPHazcomDate=excel_to_django_date(row['LastBBPHazcomDate']),
                    StateJuris=null_to_none(row['StateJuris']),
                    LastTaxModification=excel_to_django_date(row['LastTaxModification']),
                    pin=int_field(row['pin']),
                    ChangeDeliveryDate=excel_to_django_date(row['ChangeDeliveryDate']),
                    ChangeDeliveryTo=excel_to_django_date(row['ChangeDeliveryTo']),
                    addphone=null_to_none(row['addphone']),
                    EnteredBySrident=int_field(row['EnteredBySrident']),
                    LocCode=null_to_none(row['LocCode']),
                    TempMailingAddress=null_to_none(row['TempMailingAddress']),
                    TempMailingCity=null_to_none(row['TempMailingCity']),
                    TempMailingZip=null_to_none(row['TempMailingZip']),
                    TempMailingState=null_to_none(row['TempMailingState']),
                    TempMailingCountry=null_to_none(row['TempMailingCountry']),
                    TempAddressActive=null_to_none(row['TempAddressActive']),
                    SchoolDistrictCode=null_to_none(row['SchoolDistrictCode']),
                    CityCode=null_to_none(row['CityCode']),
                    CountyCode=null_to_none(row['CountyCode']),
                    HowHeardOfDetail=null_to_none(row['HowHeardOfDetail']),
                    SchoolTaxExempt=null_to_none(row['SchoolTaxExempt']),
                    CityTaxExempt=null_to_none(row['CityTaxExempt']),
                    CountyTaxExempt=null_to_none(row['CountyTaxExempt']),
                    SID=null_to_none(row['SID']),
                    AStatus=null_to_none(row['AStatus']),
                    DepartmentName=null_to_none(row['DepartmentName']),
                    CustomerId=null_to_none(row['CustomerId']),
                    CompanyName=null_to_none(row['CompanyName']),
                    ajobtitle=null_to_none(row['ajobtitle']),
                    hierid=null_to_none(row['hierid']),
                    CompanyIdent=null_to_none(row['CompanyIdent']),
                    LastAvl=null_to_none(row['LastAvl']),
                    Rating=int_field(row['Rating']),
                    PayReady=null_to_none(row['PayReady']),
                    RecordOriginId=int_field(row['RecordOriginId']),
                    DateCreated=excel_to_django_date(row['DateCreated']),
                    W4Date=excel_to_django_date(row['W4Date']),
                    ResumeDate=excel_to_django_date(row['ResumeDate']),
                    WarningFlags=null_to_none(row['WarningFlags']),
                    DefaultPayRate=decimal_field(row['DefaultPayRate']),
                    EINC=int_field(row['EINC']),
                    HierIdCC=int_field(row['HierIdCC']),
                    HierCC=int_field(row['HierCC']),
                    CPPExempt=null_to_none(row['CPPExempt']),
                    IsHouseAident=null_to_none(row['IsHouseAident']),
                    DefaultCustomerIdForAsg=null_to_none(row['DefaultCustomerIdForAsg']),
                    EIExempt=null_to_none(row['EIExempt']),
                    EEORecordExists=null_to_none(row['EEORecordExists']),
                    BypassTr=null_to_none(row['BypassTr']),
                    UnemploymentClaimDate=excel_to_django_date(row['UnemploymentClaimDate']),
                    ActiveStatus=null_to_none(row['ActiveStatus']),
                    AssignedStatus=null_to_none(row['AssignedStatus']),
                    EmployeeRootGuid=null_to_none(row['EmployeeRootGuid']),
                    DefaultPayDiff=decimal_field(row['DefaultPayDiff']),
                    SSNVerified=null_to_none(row['SSNVerified']),
                    PayMethodID=int_field(row['PayMethodID']),
                    PayDeliveryMethodID=int_field(row['PayDeliveryMethodID']),
                    ContactId=int_field(row['ContactId']),
                    employmentCategoryID=null_to_none(row['employmentCategoryID']),
                    HowHeardOfId=int_field(row['HowHeardOfId']),
                    OTPlanId=int_field(row['OTPlanId']),
                    OrderTypeId=int_field(row['OrderTypeId']),
                    TransportationTypeGUID=null_to_none(row['TransportationTypeGUID']),
                    TaxByEmployeeState=decimal_field(row['TaxByEmployeeState']),
                    ConsentToReleaseConvictions=int_field(row['ConsentToReleaseConvictions']),
                    CountryCode=int_field(row['CountryCode']),
                    SrIdent=int_field(row['SrIdent']),
                    ZipFive=int_field(row['ZipFive']),
                    has_resume=int_field(row['HasResume']),
                    user=u
                )

                # Branches
                b = Branch.objects.get(branch_name=row['BranchName'])

                t.branch.add(b)
                t.save()

                self.stdout.write('------------------------------')

def null_to_none(value):
    if value == 'NULL':
        return ''
    else:
        return value


def excel_to_django_date(date):
        if null_to_none(date):
            try:
                d = datetime.strptime(date, '%m/%d/%y %H:%M')
                return d.strftime('%Y-%m-%d %H:%M')
            except ValueError, e:
                print "TIME FORMAT NOT MATCHED:", str(e)
        else:
            return None


def int_field(value):
        value = null_to_none(value)

        if value == '':
            return None
        else:
            return int(value)


def decimal_field(value):
        value = null_to_none(value)

        if value == '':
            return None
        else:
            return float(value)