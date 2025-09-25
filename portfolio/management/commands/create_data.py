from django.core.management.base import BaseCommand
from core.models import Profile, Publication, Referee, Experience, Education, Skill, SkillCategory

class Command(BaseCommand):
    help = 'Load initial portfolio data'

    def handle(self, *args, **options):
        self.stdout.write('Loading initial portfolio data...')
        
        # Create or update profile
        profile, created = Profile.objects.update_or_create(
            name="Otieno Moses Ochieng",
            defaults={
                'title': 'Data Scientist & Statistician',
                'email': 'mosotieno25@gmail.com',
                'phone': '+254-719648375',
                'location': 'Kenya',
                'bio': 'Expert statistician and data scientist with 9+ years experience in healthcare research, data management, and programming. Specialized in HIV/AIDS research, climate change studies, and wearable technology applications. Proven track record in leading data management for major health research projects at KEMRI/CGHR.',
                'short_bio': 'Data Scientist | Statistician | Python & R Expert | Healthcare Research',
                'career_objective': 'To leverage my expertise in statistics, programming and information technology to provide innovative, data-driven solutions and effectively address complex statistical and IT challenges.',
                'years_experience': 9,
                'projects_completed': 15,
                'happy_clients': 8,
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Profile created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Profile updated successfully'))

        # Create publications
        publications_data = [
            {
                'title': 'Prevalence and risk factors of sexually transmitted infections in the setting of a generalized HIV epidemic-a population-based study, western Kenya',
                'authors': 'Ochieng MO et al.',
                'journal': 'International Journal of STD & AIDS',
                'year': 2023,
            },
            {
                'title': 'DREAMS impact on HIV status knowledge and sexual risk among cohorts of young women in Kenya and South Africa',
                'authors': 'Ochieng MO et al.',
                'journal': 'Journal of Acquired Immune Deficiency Syndromes',
                'year': 2023,
            },
            {
                'title': 'Impact of the DREAMS Partnership on social support and general self-efficacy among adolescent girls and young women: causal analysis of population-based cohorts in Kenya and South Africa',
                'authors': 'Ochieng MO et al.',
                'journal': 'BMJ Global Health',
                'year': 2022,
            },
            {
                'title': 'The long-term impact of HIV/AIDS on socio-economic status: a comparative analysis of households headed by HIV-positive and HIV-negative individuals in Western Kenya',
                'authors': 'Ochieng MO et al.',
                'journal': 'AIDS Care',
                'year': 2021,
            },
            {
                'title': 'Awareness and uptake of the Determined, Resilient, Empowered, AIDS-free, Mentored and Safe HIV prevention package over time among population-based cohorts of young women in Kenya and South Africa',
                'authors': 'Ochieng MO et al.',
                'journal': 'PLOS One',
                'year': 2020,
            }
        ]

        for i, pub_data in enumerate(publications_data):
            publication, created = Publication.objects.update_or_create(
                title=pub_data['title'],
                defaults={**pub_data, 'order': i}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Publication "{pub_data}["title][:50]..." created'))

        # Create referees
        referees_data = [
            {
                'name': 'Dr. Daniel Kwaro',
                'title': 'Branch Chief',
                'organization': 'HIV Implementation Science and Services (HISS), KEMRI-CGHR',
                'email': 'DKwaro@kemricdc.org',
                'phone': '+254 700 858 288',
                'order': 0
            },
            {
                'name': 'Dr. Sammy Khagayi',
                'title': 'Statistician',
                'organization': 'Africa Health Research Institute (AHRI)',
                'email': 'skhagayi@gmail.com',
                'phone': '+254 722 960074',
                'order': 1
            },
            {
                'name': 'Mr. George Ng\'uono Bitta',
                'title': 'Deputy Principal',
                'organization': 'Chianda High School',
                'email': 'nguonobitta@gmail.com',
                'phone': '+254 704 787 117',
                'order': 2
            }
        ]

        for ref_data in referees_data:
            referee, created = Referee.objects.update_or_create(
                name=ref_data['name'],
                defaults=ref_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Referee "{ref_data["name"]}" created'))

        # Create skill categories and skills
        categories_data = [
            {
                'name': 'Statistics & Data Science',
                'order': 0,
                'skills': [
                    {'name': 'Advanced Statistical Analysis', 'proficiency': 4, 'order': 0},
                    {'name': 'R Programming', 'proficiency': 4, 'order': 1},
                    {'name': 'Python for Data Science', 'proficiency': 3, 'order': 2},
                    {'name': 'Machine Learning', 'proficiency': 3, 'order': 3},
                    {'name': 'Reproducible Research', 'proficiency': 4, 'order': 4},
                ]
            },
            {
                'name': 'Programming & Development',
                'order': 1,
                'skills': [
                    {'name': 'Survey Solutions/ODK', 'proficiency': 4, 'order': 0},
                    {'name': 'Web Development', 'proficiency': 3, 'order': 1},
                    {'name': 'Git Version Control', 'proficiency': 3, 'order': 2},
                    {'name': 'Batch Programming', 'proficiency': 3, 'order': 3},
                    {'name': 'C/C++/C#', 'proficiency': 2, 'order': 4},
                ]
            },
            {
                'name': 'Databases',
                'order': 2,
                'skills': [
                    {'name': 'MySQL', 'proficiency': 4, 'order': 0},
                    {'name': 'PostgreSQL', 'proficiency': 3, 'order': 1},
                    {'name': 'SQL Server', 'proficiency': 3, 'order': 2},
                    {'name': 'Microsoft Access', 'proficiency': 4, 'order': 3},
                ]
            },
            {
                'name': 'Tools & Technologies',
                'order': 3,
                'skills': [
                    {'name': 'Power BI', 'proficiency': 4, 'order': 0},
                    {'name': 'Tableau', 'proficiency': 3, 'order': 1},
                    {'name': 'Stata', 'proficiency': 4, 'order': 2},
                    {'name': 'SPSS', 'proficiency': 4, 'order': 3},
                    {'name': 'Microsoft Office', 'proficiency': 4, 'order': 4},
                ]
            }
        ]

        for cat_data in categories_data:
            category, created = SkillCategory.objects.update_or_create(
                name=cat_data['name'],
                defaults={'order': cat_data['order']}
            )
            
            for skill_data in cat_data['skills']:
                skill, created = Skill.objects.update_or_create(
                    name=skill_data['name'],
                    category=category,
                    defaults={
                        'proficiency': skill_data['proficiency'],
                        'order': skill_data['order'],
                        'show_on_main': True
                    }
                )
            
            self.stdout.write(self.style.SUCCESS(f'Category "{cat_data["name"]}" and skills created'))

        # Create experiences
        experiences_data = [
            {
                'title': 'Data Manager & Statistician',
                'company': 'KEMRI/CGHR',
                'location': 'Kenya',
                'experience_type': 'job',
                'start_date': '2025-02-01',
                'current': True,
                'description': 'Implementation of Point of Care HIV Viral Load Monitoring to improve Viral Load Suppression among Children and Adolescents Living with HIV in East Africa. (EAPoC-VL)',
                'responsibilities': """• Conducted routine data cleaning and validation to ensure accuracy, consistency, and readiness of datasets for analysis.
• Generated reports and queries from data cleaning processes to enhance data understanding and collaborated with project teams to resolve emerging data issues.
• Partnered with statisticians to produce high-level statistical outputs. Contributed to the publication committee by providing statistical input and support for manuscripts.""",
                'order': 0
            },
            {
                'title': 'Data Scientist',
                'company': 'KEMRI/CGHR',
                'location': 'Kenya',
                'experience_type': 'job',
                'start_date': '2024-10-01',
                'end_date': '2024-11-30',
                'description': 'Climate Change and Wearable Technology: Assessing the Impact on Malaria and HIV in Siaya, Kenya',
                'responsibilities': """• Designed and deployed mobile data collection systems using Survey Solutions, ensuring seamless field data capture and synchronization.
• Utilized Python and R for data cleaning, wrangling, and preprocessing, ensuring high-quality and actionable datasets for analysis.
• Created automated workflows in R and Python to generate detailed progress reports, streamlining monitoring and evaluation processes.
• Collaborated with field teams to troubleshoot data collection issues and optimize workflows for efficiency.""",
                'order': 1
            },
            # Add more experiences as needed
        ]

        for exp_data in experiences_data:
            experience, created = Experience.objects.update_or_create(
                title=exp_data['title'],
                company=exp_data['company'],
                start_date=exp_data['start_date'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Experience "{exp_data["title"]}" created'))

        # Create education
        education_data = [
            {
                'degree': 'Bachelor of Science in Mathematics (Statistics Option)',
                'institution': 'Masinde Muliro University of Science and Technology',
                'location': 'Kenya',
                'start_date': '2012-09-01',
                'end_date': '2016-12-31',
                'description': 'Focused on statistical methods, data analysis, and mathematical modeling.',
                'order': 0
            },
            {
                'degree': 'Kenya Certificate of Secondary Education',
                'institution': 'Chianda High School',
                'location': 'Kenya',
                'start_date': '2008-01-01',
                'end_date': '2011-11-30',
                'grade': 'B+',
                'order': 1
            }
        ]

        for edu_data in education_data:
            education, created = Education.objects.update_or_create(
                degree=edu_data['degree'],
                institution=edu_data['institution'],
                defaults=edu_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Education "{edu_data["degree"]}" created'))

        self.stdout.write(self.style.SUCCESS('Initial data loading completed successfully!'))