from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from books.models import Book

class Command(BaseCommand):
    help = 'Populate the database with 10 sample books'  # quick way to get test data

    def handle(self, *args, **options):
        # We need a user to own these books - let's make an admin if one doesn't exist
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'admin@bookstore.com'}
        )
        if created:
            user.set_password('admin123')  # TODO: change this in production!
            user.save()
            self.stdout.write(self.style.SUCCESS('Created admin user'))

        # Start fresh - remove any existing books
        Book.objects.all().delete()
        self.stdout.write('Cleared existing books')

        # Hand-picked collection of good books for testing
        books_data = [
            {
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee', 
                'year': 1960,
                'rating': 4.8,
                'description': 'A gripping tale of racial injustice and childhood innocence in the American South. This timeless classic explores themes of morality, justice, and human dignity through the eyes of Scout Finch.'
            },
            {
                'title': '1984',
                'author': 'George Orwell',
                'year': 1949,
                'rating': 4.7,
                'description': 'A dystopian masterpiece depicting a totalitarian society where Big Brother watches everything. Orwell\'s chilling vision of surveillance and thought control remains eerily relevant today.'
            },
            {
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'year': 1813,
                'rating': 4.6,
                'description': 'A witty romance between Elizabeth Bennet and Mr. Darcy set in Regency England. Austen\'s sharp social commentary and memorable characters make this a beloved classic.'
            },
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'year': 1925,
                'rating': 4.4,
                'description': 'A tale of wealth, love, and the American Dream in the Jazz Age. Nick Carraway narrates the tragic story of Jay Gatsby\'s obsession with the beautiful Daisy Buchanan.'
            },
            {
                'title': 'Harry Potter and the Philosopher\'s Stone',
                'author': 'J.K. Rowling',
                'year': 1997,
                'rating': 4.9,
                'description': 'The magical beginning of Harry Potter\'s journey at Hogwarts School of Witchcraft and Wizardry. A young wizard discovers his true heritage and faces the dark wizard who killed his parents.'
            },
            {
                'title': 'The Catcher in the Rye',
                'author': 'J.D. Salinger',
                'year': 1951,
                'rating': 4.2,
                'description': 'Holden Caulfield\'s rebellious journey through New York City captures the angst and alienation of teenage life. A controversial yet influential coming-of-age story.'
            },
            {
                'title': 'Lord of the Rings: The Fellowship of the Ring',
                'author': 'J.R.R. Tolkien',
                'year': 1954,
                'rating': 4.8,
                'description': 'Epic fantasy adventure following Frodo Baggins as he begins his quest to destroy the One Ring. Tolkien creates a rich world of hobbits, elves, dwarves, and dark forces.'
            },
            {
                'title': 'The Hunger Games',
                'author': 'Suzanne Collins',
                'year': 2008,
                'rating': 4.5,
                'description': 'In a dystopian future, Katniss Everdeen volunteers for a deadly televised competition to save her sister. A thrilling tale of survival, rebellion, and sacrifice.'
            },
            {
                'title': 'Dune',
                'author': 'Frank Herbert',
                'year': 1965,
                'rating': 4.6,
                'description': 'Set on the desert planet Arrakis, this science fiction masterpiece follows Paul Atreides as he navigates political intrigue, mystical powers, and ecological themes in a far-future universe.'
            },
            {
                'title': 'The Da Vinci Code',
                'author': 'Dan Brown',
                'year': 2003,
                'rating': 4.1,
                'description': 'A thrilling mystery combining art, history, and religion as symbologist Robert Langdon unravels a conspiracy involving the Holy Grail and secret societies.'
            }
        ]

        # Create books
        books_created = 0
        for book_data in books_data:
            book = Book.objects.create(
                user=user,
                **book_data
            )
            books_created += 1
            self.stdout.write(f'Created: {book.title} by {book.author}')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {books_created} sample books!')
        )
        self.stdout.write(
            self.style.WARNING('Admin user credentials: username=admin, password=admin123')
        )